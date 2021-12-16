import logging
import socket
from pathlib import Path

from client.core.Api import Api
from client.core.ModuesLoader import ModulesLoader


class Client:
    hostname: str
    api: Api
    moduleLoader: ModulesLoader
    configVer: int
    timeout: int

    def __init__(self):
        print("Initialization of client")
        self.hostname = socket.gethostname()
        self.api = Api()

        # print("Getting config from master")
        # data = self.api.register(self.hostname)
        # self.configVer = data['id']
        # self.timeout = data['timeout']

        # print("Checking modules and download if needed")
        # Path("./client/modules").mkdir(parents=True, exist_ok=True)
        # print("Initialization of Modules Loader")
        # self.moduleLoader = ModulesLoader(data['modules'])
        # print("Client initialization ok")
        # print("Entering into main loop")
        print("Client init success starting Celery worker")
