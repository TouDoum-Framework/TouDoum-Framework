from django.db import models


class Config(models.Model):
    pluginEnabled = models.TextField()
    skipPrivate = models.BooleanField()
    timeout = models.IntegerField()
    createdAt = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.id)


class Worker(models.Model):
    uuid = models.CharField(max_length=64)
    currentConfig = models.ForeignKey(Config, on_delete=models.DO_NOTHING, blank=True, null=True)
    createdAt = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.uuid


class Addr(models.Model):
    ip = models.CharField(max_length=32)
    ipType = models.IntegerField()  # 4 or 6
    rescanPriority = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ip


class LogEvent(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
    ip = models.ForeignKey(Addr, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=64)
    createdAt = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.id)


class ScanResult(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
    ip = models.ForeignKey(Addr, on_delete=models.DO_NOTHING)
    result = models.TextField()
    configVer = models.ForeignKey(Config, on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.result
