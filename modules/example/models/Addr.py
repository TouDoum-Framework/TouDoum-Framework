from django.db import models
from iptools import IpRangeList

from server.modules.models import Module

ip_private = IpRangeList(
    '0.0.0.0/8', '10.0.0.0/8', '100.64.0.0/10', '127.0.0.0/8',
    '169.254.0.0/16', '172.16.0.0/12', '192.0.0.0/24', '192.0.2.0/24',
    '192.88.99.0/24', '192.168.0.0/16', '198.18.0.0/15', '198.51.100.0/24',
    '203.0.113.0/24', '224.0.0.0/4', '240.0.0.0/4', '255.255.255.255/32',
    'fc00::/7', 'fec0::/10'
)


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
