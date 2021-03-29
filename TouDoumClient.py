import os
import socket
from pathlib import Path

from dotenv import load_dotenv

from client.Api import Api
from client.PluginManager import PluginManager


class Client:
    hostname: str
    api: Api
    pluginManager: PluginManager
    configVer: int
    skipPrivate: bool
    timeout: int

    def __init__(self):
        print("Initialization of client")
        self.hostname = socket.gethostname()
        self.api = Api()

        print("Getting config from master")
        data = self.api.register(self.hostname)
        self.configVer = data['id']
        self.skipPrivate = data['skipPrivate']
        self.timeout = data['timeout']

        print("Checking plugin and download if needed")
        Path("./client/plugins").mkdir(parents=True, exist_ok=True)
        print("Initialization of Plugin Manager")
        self.pluginManager = PluginManager(data['plugins'])
        if len(self.pluginManager.download) > 0:
            print("Downloading missing plugins")
            self.api.download(self.pluginManager.download)
            self.pluginManager.reload(data['plugins'])
            print("All plugins have been downloaded and loaded into the client")
        else:
            print("All the plugins already exist")

        print("Client initialization ok")
        print("Entering into main loop")

    def loop(self):
        while True:
            data = self.api.getIP()
            if data is not None:

                result = {
                    "ip": data['ip'],
                    "worker": self.hostname,
                    "config": self.configVer,
                    "result": {}
                }

                for plugin in self.pluginManager.plugins:
                    print("Scanning ip " + data['ip'] + " with plugin " + plugin.name)
                    result['result'][plugin.name] = bool(plugin.scan(ip=data['ip'], timeout=self.timeout))

                self.api.save(result)


if __name__ == '__main__':
    if os.environ.get("MODE") is None:
        load_dotenv(".env")
        print("Load env from .env file")
    else:
        print("Not using .env file")

    client = Client()
    client.loop()
