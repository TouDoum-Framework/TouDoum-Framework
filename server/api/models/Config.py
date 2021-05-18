from django.http import JsonResponse
from django.core.cache import cache
from django.db import models

from server.api import ErrorCode
from server.modules.models import Module


class Config(models.Model):
    pause = models.BooleanField(default=False)
    modulesEnabled = models.ManyToManyField(Module)
    skipPrivate = models.BooleanField(default=True)
    timeout = models.IntegerField()
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str((self.id, self.skipPrivate, self.timeout))


def get_last_config() -> Config or None:
    try:
        config: Config = cache.get("config")
        if not config:
            config = Config.objects.latest("createdAt")
            cache.set("config", config)
        return config
    except Config.DoesNotExist:
        return None


def last_config() -> JsonResponse:
    config_obj: Config = get_last_config()

    if config_obj is None:
        return ErrorCode.NoneConfigExist()

    reply_config = {
        'id': config_obj.id,
        'modules': [mod.name for mod in config_obj.modulesEnabled.all()],
        'timeout': config_obj.timeout
    }
    return JsonResponse(reply_config, safe=False)


def get_enabled_modules() -> list:
    config: Config = get_last_config()
    return config.modulesEnabled.split(",")
