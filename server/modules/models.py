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


class ModuleFile(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    checksum = models.CharField(max_length=255)
    module = models.ForeignKey(Module, related_name="modules", on_delete=models.CASCADE)
    is_client = models.BooleanField()

    def __str__(self):
        return str(self.path)
