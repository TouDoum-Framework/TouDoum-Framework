from django.db import models

from server.modules.models import Module


class Config(models.Model):
    pause = models.BooleanField(default=False)
    modules_enabled = models.ManyToManyField(Module)
    skip_private = models.BooleanField(default=True)
    timeout = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


def get_last_config() -> Config or None:
    try:
        config = Config.objects.latest("created_at")
        return config
    except Config.DoesNotExist:
        return None


def get_enabled_modules() -> list:
    config: Config = get_last_config()
    return config.modules_enabled.split(",")
