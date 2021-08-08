from rest_framework import viewsets, permissions

from server.api.serializers import ModuleSerializer
from server.modules.models import Module


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all().order_by("id")
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]
