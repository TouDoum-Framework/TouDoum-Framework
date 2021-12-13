from celery import Celery
from server.celery import debug_task
app = Celery('tasks', broker='pyamqp://white:neo@localhost//')
