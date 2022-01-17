from rest_framework import viewsets, permissions

from server.api.serializers import ModuleFileSerializer
from server.modules.models import ModuleFile


class ModuleFileViewSet(viewsets.ModelViewSet):
    queryset = ModuleFile.objects.all().order_by("id")
    serializer_class = ModuleFileSerializer
    permission_classes = [permissions.IsAuthenticated]
