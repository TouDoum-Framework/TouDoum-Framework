from django.db import models


class Config(models.Model):
    pluginEnabled = models.TextField()
    skipPrivate = models.BooleanField()
    timeout = models.IntegerField()


class Worker(models.Model):
    createdAt = models.DateTimeField()
    currentConfig = models.ForeignKey(Config, on_delete=models.DO_NOTHING)
    lastRequest = models.DateTimeField()


class Addr(models.Model):
    ip = models.CharField(max_length=32)
    ipType = models.IntegerField()  # 4 or 6
    rescanPriority = models.IntegerField()


class LogEvent(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
    ip = models.ForeignKey(Addr, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=64)
    createdAt = models.DateTimeField()


class ScanResult(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
    ip = models.ForeignKey(Addr, on_delete=models.DO_NOTHING)
    result = models.TextField()
    createdAt = models.DateTimeField()
