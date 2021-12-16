from django.db import models


class Module(models.Model):
    name = models.CharField(max_length=64)
    version = models.CharField(max_length=64)
    depend_on = models.ManyToManyField('self')

    def __str__(self):
        return str(self.name)
