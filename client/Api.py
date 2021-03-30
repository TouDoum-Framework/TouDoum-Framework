import json
import os
import requests
import time


class Api:
    url: str
    token: str

    def __init__(self):
        self.url = os.environ.get('API_URL')
        self.token = os.environ.get('TOKEN')

    def register(self, hostname: str):
        print("Try to register client")
        headers = {'Authorization': self.token}
        data = {"hostname": hostname}
        reply = requests.post(self.url + "/worker", json=data, headers=headers)
        if reply.status_code == 501:
            print("Client registered, but no config return by master waiting 60s and retry")
            time.sleep(60)
            self.register(hostname)
        elif reply.status_code == 200:
            print("Client registered and config hase been receives")
            return json.loads(reply.text)
        else:
            return exit(-1)

    def download(self, download: list):
        for plugin in download:
            print("Downloading plugin " + plugin)
            headers = {'Authorization': self.token}
            reply = requests.get(self.url + "/config/" + plugin, headers=headers)
            file = open("./client/plugins/" + plugin + ".py", "w")
            file.write(reply.text)
            file.close()

    def getIP(self):
        print("Getting ip to scan")
        headers = {'Authorization': self.token}
        reply = requests.get(self.url + "/addr", headers=headers)
        if reply.status_code == 200:
            data = json.loads(reply.text)
            print("Ip " + data['ip'] + " receives")
            return data
        return None

    def save(self, result):
        print("Saving scan result")
        headers = {'Authorization': self.token}
        reply = requests.post(self.url + "/addr", json=result, headers=headers)
        print("Save Ok")
