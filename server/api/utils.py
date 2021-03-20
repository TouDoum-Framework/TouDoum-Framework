from django.http import JsonResponse

from server.api.models import Config
from server.core import ErrorCode


def get_last_config():
    config_obj: Config = Config.objects.last()
    return config_obj


def last_config() -> JsonResponse:
    config_obj: Config = Config.objects.last()
    if config_obj is None:
        return ErrorCode.NoneConfigExist()

    reply_config = {
        'id': config_obj.id,
        'pluginEnabled': config_obj.pluginEnabled,
        'skipPrivate': config_obj.skipPrivate,
        'timeout': config_obj.timeout
    }
    return JsonResponse(reply_config, safe=False)
