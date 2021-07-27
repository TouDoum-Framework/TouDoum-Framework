from django.db import models
from server.api.models.Config import Config


class Worker(models.Model):
    uuid = models.CharField(max_length=64)
    currentConfig = models.ForeignKey(Config, on_delete=models.DO_NOTHING, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.uuid, self.currentConfig))
