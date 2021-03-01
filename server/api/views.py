from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from core.utils import load_data, EventName
from server.api.models import *


@csrf_exempt
def index(request: HttpRequest):
    return JsonResponse("Hummm", safe=False)


@csrf_exempt
def worker(request: HttpRequest):
    return JsonResponse({}, safe=False)


def config(request: HttpRequest):
    return JsonResponse(None, safe=False)


def config_get(request: HttpRequest, ver: int):
    return JsonResponse(ver, safe=False)


def config_get_plugin(request: HttpRequest, ver: int, plugin: str):
    return JsonResponse(None, safe=False)


def addr(request: HttpRequest):
    return JsonResponse(None, safe=False)
