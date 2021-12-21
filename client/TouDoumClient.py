from socket import gethostname
from os import environ
from celery import Celery
from dotenv import load_dotenv

from client.core.Api import Api
from client.core.ModuesLoader import ModulesLoader


class Client:
    hostname: str
    api: Api
    moduleLoader: ModulesLoader
    celery: Celery

    def __init__(self, celery):
        print("Initialization of client")
        self.hostname = gethostname()
        self.api = Api()
        self.celery = celery

        print("Client init success starting Celery worker")


if environ.get("MODE") is None:
    load_dotenv("../.env")
    print("Load env from .env file")

celery = Celery('tasks', broker='pyamqp://{}:{}@{}//'.format(
    environ.get("MQ_USER", "white"),
    environ.get("MQ_PASS", "neo"),
    environ.get("MQ_HOST", "127.0.0.1")
))
celery.autodiscover_tasks(['client.core'])
#client = Client(celery)
