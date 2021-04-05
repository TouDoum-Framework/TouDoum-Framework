import json
from datetime import datetime

from django.http import JsonResponse, HttpRequest, FileResponse
from django.views.decorators.csrf import csrf_exempt

from server.core.PluginManager import PluginManager

from server.api.utils import last_config, get_last_config
from server.core import TokenAuthentication, ErrorCode
from server.core.ResultManager import ResultManger
from server.api.models import Addr, Worker


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
        pm = PluginManager()
        for p in pm.plugins:
            if plugin == p.name:
                file = open("plugins/" + p.file + ".py", 'rb')
                response = FileResponse(file)
                return response
        return ErrorCode.PluginDoesNotExist()
    else:
        return TokenAuthentication.error()


@csrf_exempt
def addr(request: HttpRequest):
    if TokenAuthentication.is_token_valid(request):
        if request.method == 'GET':

            ip = Addr.objects.all().filter(used=False).order_by("-rescanPriority", "lastUpdate").first()
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
        return last_config()
    else:
        return TokenAuthentication.error()
