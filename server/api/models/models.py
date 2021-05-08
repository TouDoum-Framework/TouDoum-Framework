from django.db import models
from server.api.models.Config import Config
from server.modules.models import Module


class Worker(models.Model):
    uuid = models.CharField(max_length=64)
    currentConfig = models.ForeignKey(Config, on_delete=models.DO_NOTHING, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.uuid, self.currentConfig))


class Addr(models.Model):
    ip = models.CharField(unique=True, max_length=32)
    isPrivate = models.BooleanField(default=False)
    rescanPriority = models.IntegerField(blank=True, default=0)
    used = models.BooleanField(default=False)
    modules = models.ManyToManyField(Module, blank=True)
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.ip, self.rescanPriority))
