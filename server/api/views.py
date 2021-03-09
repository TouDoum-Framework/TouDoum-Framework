import json

from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from server.api.utils import getLastConfig
from server.core import TokenAuthentication, ErrorCode
from server.api.models import *


@csrf_exempt
def index(request: HttpRequest):
    return JsonResponse("Hummm", safe=False)


@csrf_exempt
def worker(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):

        if request.method == 'POST':
            worker_obj: Worker = Worker.objects.last()
            data = json.loads(request.body)
            if worker_obj is None:
                new_worker = Worker()
                new_worker.uuid = data['hostname']
                new_worker.save()

            return JsonResponse(getLastConfig(), safe=False)
        else:
            return ErrorCode.badMethod()
    else:
        return TokenAuthentication.error()


def config(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        return JsonResponse(getLastConfig(), safe=False)
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
