from os import environ
from celery import Celery

app = Celery('tasks',  broker='pyamqp://{}:{}@{}//'.format(
    environ.get("MQ_HOST", "127.0.0.1"),
    environ.get("MQ_USER", "white"),
    environ.get("MQ_PASS", "neo")
))


@app.task(bind=True)
def client_exec():
    from client.TouDoumClient import Client
    print("hey")
