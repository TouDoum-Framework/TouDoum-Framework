import json

from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from server.api.utils import last_config, get_last_config
from server.core import TokenAuthentication, ErrorCode
from server.api.models import *


@csrf_exempt
def index(request: HttpRequest):
    return JsonResponse("Hummm", safe=False)


@csrf_exempt
def worker(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            worker_obj: Worker = Worker.objects.filter(uuid=data['hostname']).last()
            if worker_obj is None:
                new_worker = Worker()
                new_worker.uuid = data['hostname']
                new_worker.currentConfig = get_last_config()
                new_worker.save()
                return last_config()

            worker_obj.currentConfig = get_last_config()
            worker_obj.save()
            return last_config()
        else:
            return ErrorCode.badMethod()
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
