import iptools
from django.http import HttpResponseRedirect
from rest_framework import viewsets, permissions

from modules.example.models.Addr import Addr
from modules.example.serializers import AddrSerializer


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
