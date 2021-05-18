import json
from datetime import datetime

from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from server.api.models import Config

from server.api import ErrorCode
from server.core.ResultManager import ResultManger
from server.api.models.models import Addr, Worker
from server.core import TokenAuthentication
from server.modules.apps import get_client_file, download_client_file


@csrf_exempt
def register(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            worker_obj: Worker = Worker.objects.filter(uuid=data['hostname']).last()
            if worker_obj is None:
                new_worker = Worker()
                new_worker.uuid = data['hostname']
                new_worker.currentConfig = Config.get_last_config()
                new_worker.save()
                return Config.last_config()
            worker_obj.currentConfig = Config.get_last_config()
            worker_obj.save()
            return Config.last_config()
        else:
            return ErrorCode.badMethod()
    else:
        return TokenAuthentication.error()


def modules_discovery(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        return JsonResponse(Config.get_enabled_modules(), safe=False)
    else:
        return TokenAuthentication.error()

@csrf_exempt
def module_discovery_by_name(request: HttpRequest, module: str):
    if request.method == "GET":
        return JsonResponse(json.dumps(get_client_file(module)), safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        return download_client_file(module, data["file"])


# todo change save function look at notion.so dashboard
@csrf_exempt
def addr(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        config = Config.last_config()
        if request.method == 'GET':
            if config["skipPrivate"]:
                ip = Addr.objects.all().filter(used=False).order_by("-rescanPriority", "lastUpdate").first()
            else:
                ip = Addr.objects.all().filter(used=False, isPrivate=False).order_by("-rescanPriority",
                                                                                     "lastUpdate").first()
            ip.lastUpdate = datetime.now()
            ip.rescanPriority = 0
            ip.used = True
            ip.save()
            return JsonResponse({"ip": ip.ip}, safe=False)

        elif request.method == 'POST':

            data = json.loads(request.body)

            ip = Addr.objects.filter(ip=data["ip"]).first()
            ip.lastUpdate = datetime.now()
            ip.rescanPriority = 0
            ip.used = False
            ip.save()

            rm = ResultManger()
            rm.save(data)

        else:
            return ErrorCode.badMethod()
        return config
    else:
        return TokenAuthentication.error()
