from django.db import models


class Config(models.Model):
    pause = models.BooleanField(default=False)
    pluginEnabled = models.TextField()
    skipPrivate = models.BooleanField(default=True)
    timeout = models.IntegerField()
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.id, self.skipPrivate, self.timeout))


class Worker(models.Model):
    uuid = models.CharField(max_length=64)
    currentConfig = models.ForeignKey(Config, on_delete=models.DO_NOTHING, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.uuid, self.currentConfig))


class Addr(models.Model):
    ip = models.CharField(unique=True, max_length=32)
    rescanPriority = models.IntegerField(blank=True, default=0)
    used = models.BooleanField(default=False)
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.ip, self.rescanPriority))
