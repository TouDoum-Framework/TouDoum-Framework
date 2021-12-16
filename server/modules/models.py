from django.db import models


class Module(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    version = models.IntegerField()
    depend_on = models.ManyToManyField('self')
    author = models.CharField(max_length=255)
    repo = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
