import json
from datetime import datetime

from django.http import JsonResponse, HttpRequest, FileResponse
from django.views.decorators.csrf import csrf_exempt

from core.manager.PluginManager import PluginManager

from server.api.utils import last_config, get_last_config
from server.core import TokenAuthentication, ErrorCode
from server.api.models import *


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

            ips = Addr.objects.all().order_by("-rescanPriority", "lastUpdate")[0:10]
            for ip in ips:
                print(ip.ip)
                event = AddrEvent.objects.all().filter(ip=ip).order_by("createdAt")[0:5]
                for e in event:
                    if e.status == "free":

                        ip.lastUpdate = datetime.now()
                        ip.rescanPriority = 0
                        ip.save()

                        newEvent = AddrEvent()
                        newEvent.ip = ip
                        newEvent.status = "used"
                        newEvent.save()
                        return JsonResponse({"ip": ip.ip}, safe=False)

        elif request.method == 'POST':

            data = json.loads(request.body)

            ip = Addr.objects.filter(ip=data["ip"]).last()
            ip.rescanPriority = 0

            newEvent = AddrEvent()
            newEvent.ip = ip
            newEvent.status = "free"

            scanResult = ScanResult()
            scanResult.ip = ip
            scanResult.worker = Worker.objects.filter(uuid=data["worker"]).last()
            scanResult.configVer = Config.objects.filter(pk=data["config"]).last()
            scanResult.result = data["result"]

            newEvent.save()
            ip.save()
            scanResult.save()

        else:
            return ErrorCode.badMethod()
        return JsonResponse({}, safe=False)
    else:
        return TokenAuthentication.error()
