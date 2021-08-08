from rest_framework import viewsets, permissions

from server.api.serializers import MasterSerializer
from server.cluster.models.Master import Master


class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all().order_by("id")
    serializer_class = MasterSerializer
    permission_classes = [permissions.IsAuthenticated]
