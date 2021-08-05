from django.db import models


class Master(models.Model):
    uuid = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uuid)
