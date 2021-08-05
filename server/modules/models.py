from django.db import models

from server.cluster.models.Master import Master


class Module(models.Model):
    name = models.CharField(max_length=64)
    version = models.CharField(max_length=64)
    availableAt = models.ManyToManyField(Master)

    def __str__(self):
        return str(self.id)
