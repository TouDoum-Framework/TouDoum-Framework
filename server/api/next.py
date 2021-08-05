from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

import iptools

from server.api.serializers import *
from server.api.models.Addr import Addr


def nextBrowsableAPI(request: HttpRequest):
    return render(request, 'browsable.html')


class AddrViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Addr to be viewed or edited.
    """
    queryset = Addr.objects.all().order_by("-scan_priority", "last_update")
    serializer_class = AddrSerializer
    permission_classes = [permissions.IsAuthenticated]

    # we can add list of ip by cidr
    def create(self, request, **kwargs):
        addrs = []
        ip_list = iptools.IpRangeList(request.data["ip"]).__iter__()
        try:
            while True:
                addr = Addr()
                addr.ip = iptools.next(ip_list)
                addr.scan_priority = int(request.data["scan_priority"])
                addr.save()
                addrs.append(addr)
        except StopIteration:
            pass
        return HttpResponseRedirect(self.request.path_info)


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all().order_by("id")
    serializer_class = ConfigSerializer
    permission_classes = [permissions.IsAuthenticated]


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all().order_by("id")
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]