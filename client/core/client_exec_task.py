from celery import Celery

app = Celery('tasks', broker='pyamqp://white:neo@localhost//')


@app.task(bind=True)
def client_exec():
    from client.TouDoumClient import Client
    print("hey")
