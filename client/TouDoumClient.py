import sys
from os import environ

from celery import Celery
from dotenv import load_dotenv

from client.core.TouDoumWorker import TouDoumWorker

if environ.get("MODE") is None:
    load_dotenv(".env")
    print("Load env from .env file")

celery = Celery('tasks', broker='pyamqp://{}:{}@{}//'.format(
    environ.get("MQ_USER", "white"),
    environ.get("MQ_PASS", "neo"),
    environ.get("MQ_HOST", "127.0.0.1")
))
celery.autodiscover_tasks(['client.core'])
tdw = TouDoumWorker()
tdw.set_celery_instance(celery)

if __name__ == '__main__':
    print("Error: to run the celery worker please run this command or refer to the documentation")
    print("Error: > celery -A client.TouDoumClient worker")
    sys.exit()
