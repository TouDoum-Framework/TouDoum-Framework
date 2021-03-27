from django.db import models


class Config(models.Model):
    pluginEnabled = models.TextField()
    skipPrivate = models.BooleanField()
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
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.ip, self.rescanPriority))


class AddrEvent(models.Model):
    ip = models.ForeignKey(Addr, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=64)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.ip.ip, self.status))


class ScanResult(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
    ip = models.ForeignKey(Addr, on_delete=models.DO_NOTHING)
    result = models.TextField()
    configVer = models.ForeignKey(Config, on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.worker.uuid, self.ip.ip, self.configVer.id))
