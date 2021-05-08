from django.http import JsonResponse, HttpRequest, FileResponse

from server.api import ErrorCode
from server.core import TokenAuthentication
from server.modules.src.plugins.PluginManager import PluginManager


def discovery(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        return JsonResponse({}, status=200)
    return TokenAuthentication.error()


def config_get_plugin(request: HttpRequest, plugin: str):
    if TokenAuthentication.is_token_valid(request):
        pm = PluginManager()
        for p in pm.plugins:
            if plugin == p.name:
                file = open("plugins/" + p.file + ".py", 'rb')
                response = FileResponse(file)
                return response
        return ErrorCode.PluginDoesNotExist()
    else:
        return TokenAuthentication.error()
