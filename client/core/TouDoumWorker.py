from __future__ import annotations
from socket import gethostname

from celery import Celery

from client.core.Singleton import Singleton
from client.core.Api import Api
from client.core.ModuesLoader import ModulesLoader


class TouDoumWorker(Singleton):
    hostname: str
    api: Api
    moduleLoader: ModulesLoader
    celery: Celery

    def __init__(self):
        self.hostname = gethostname()
        self.api = Api()

    def set_celery_instance(self, celery_instance) -> TouDoumWorker:
        self.celery = celery_instance
        return self
