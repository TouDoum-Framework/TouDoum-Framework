from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from server.core import TokenAuthentication
from server.api.models import *


@csrf_exempt
def index(request: HttpRequest):
    return JsonResponse("Hummm", safe=False)


@csrf_exempt
def worker(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        return JsonResponse({}, safe=False)
    else:
        return TokenAuthentication.error()


def config(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        return JsonResponse({}, safe=False)
    else:
        return TokenAuthentication.error()


def config_get_plugin(request: HttpRequest, plugin: str):
    if TokenAuthentication.is_token_valid(request):
        return JsonResponse({}, safe=False)
    else:
        return TokenAuthentication.error()


def addr(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        return JsonResponse({}, safe=False)
    else:
        return TokenAuthentication.error()
