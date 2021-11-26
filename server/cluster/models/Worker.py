from django.db import models
from server.api.models.Config import Config


class Worker(models.Model):
    uuid = models.CharField(max_length=64)
    current_config = models.ForeignKey(Config, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uuid)
