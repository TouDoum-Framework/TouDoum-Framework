from rest_framework import viewsets, permissions

from server.api.serializers import ModuleSerializer
from server.modules.models import ModuleClientFile


class ModuleClientFileViewSet(viewsets.ModelViewSet):
    queryset = ModuleClientFile.objects.all().order_by("id")
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]
