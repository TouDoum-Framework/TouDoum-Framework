from django.contrib import admin
from server.cluster.models.Master import Master
from server.cluster.models.Worker import Worker

admin.site.register(Master)
admin.site.register(Worker)
