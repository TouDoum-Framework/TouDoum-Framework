from os import environ

from celery import Celery

# Set the default Django settings module for the 'celery' program.
environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('tasks',  broker='pyamqp://{}:{}@{}//'.format(
    environ.get("MQ_USER", "white"),
    environ.get("MQ_PASS", "neo"),
    environ.get("MQ_HOST", "127.0.0.1")
))

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

from client.core.client_exec_task import client_exec