import json
import os
from base64 import b64decode
from pathlib import Path

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
        try:
            reply = requests.post(self.url + "/register", json=data, headers=headers)
            if reply.status_code == 501:
                print("Client registered, but no config return by master waiting 60s and retry")
                time.sleep(60)
                self.register(hostname)
            elif reply.status_code == 200:
                print("Client registered and config hase been receives")
                return json.loads(reply.text)
            else:
                print("Return type error " + reply.status_code)
                print("Check server logs")
                return exit(-1)
        except requests.exceptions.ConnectionError:
            print("Enable to connect to master waiting 60s and retry")
            time.sleep(60)
            self.register(hostname)

    def get_modules_from_list(self, modules: list):
        for module_name in modules:
            Path("./client/modules/" + module_name).mkdir(parents=True, exist_ok=True)
            print("Getting list of client file for module " + module_name)
            headers = {'Authorization': self.token}
            reply = requests.get(self.url + "/module/" + module_name + "/client", headers)
            print("List received downloading")
            for file in json.loads(reply.text):
                file_name = b64decode(file.encode('ascii')).decode('ascii')
                print("Downloading " + file_name)
                r = requests.get(self.url + "/module/" + module_name + "/client/" + file, headers)
                buffer = open("client/modules/" + module_name + "/" + file_name, "w")
                buffer.write(r.text)
                buffer.close()

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
