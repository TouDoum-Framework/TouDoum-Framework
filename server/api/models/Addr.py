from django.db import models

from server.modules.models import Module
from server.core.static import ip_private


class Addr(models.Model):
    ip = models.CharField(unique=True, max_length=32)
    is_private = models.BooleanField(default=False)
    scan_priority = models.IntegerField(blank=True, default=0)
    used = models.BooleanField(default=False)
    modules = models.ManyToManyField(Module, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.ip, self.scan_priority))

    def save(self, *args, **kwargs):
        self.is_private = self.ip in ip_private
        super(Addr, self).save(*args, **kwargs)
