from django.db import models
from iptools import IpRangeList

from server.api.models.Config import Config

ip_private = IpRangeList(
    '0.0.0.0/8', '10.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12', '192.0.0.0/24', '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4', '240.0.0.0/4', '255.255.255.255/32'
)


class Worker(models.Model):
    uuid = models.CharField(max_length=64)
    currentConfig = models.ForeignKey(Config, on_delete=models.DO_NOTHING, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.uuid, self.currentConfig))


class Addr(models.Model):
    ip = models.CharField(unique=True, max_length=32)
    isPrivate = models.BooleanField(default=False)
    rescanPriority = models.IntegerField(blank=True, default=0)
    used = models.BooleanField(default=False)
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.ip, self.rescanPriority))
