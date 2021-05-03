from django.http import JsonResponse
from django.core.cache import cache

from server.api.models import Config
from server.api import ErrorCode


def get_last_config() -> Config:
    config_obj: Config = cache.get("config")

    if not config_obj:
        config_obj = Config.objects.latest("createdAt")
        cache.set("config", config_obj)

    return config_obj


def last_config() -> JsonResponse:
    config_obj: Config = get_last_config()

    if config_obj is None:
        return ErrorCode.NoneConfigExist()

    reply_config = {
        'id': config_obj.id,
        'plugins': config_obj.modulesEnabled.split(","),
        'skipPrivate': config_obj.skipPrivate,
        'timeout': config_obj.timeout
    }
    return JsonResponse(reply_config, safe=False)
