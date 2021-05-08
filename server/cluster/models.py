from django.db import models


class Master(models.Model):
    uuid = models.CharField(max_length=64)
    createdAt = models.DateTimeField(auto_created=True)
    lastUpdate = models.DateTimeField(auto_now=True)
