from django.http import Http404, FileResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from server.api.serializers import ModuleFileSerializer
from server.modules.models import Module, ModuleFile


class ModuleFileViewSet(viewsets.ModelViewSet):
    queryset = ModuleFile.objects.all().order_by("id")
    serializer_class = ModuleFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = ModuleFile.objects.all()
        module_name = self.request.query_params.get("module")
        file_hash = self.request.query_params.get("hash")
        if module_name is not None:
            module = Module.objects.filter(name=module_name).first()
            queryset = queryset.filter(module=module)
        if file_hash is not None:
            queryset = queryset.filter(hash=file_hash)
        return queryset

    @action(detail=False)
    def download(self, request):
        module_file: ModuleFile = self.get_queryset().first()
        if module_file is None:
            raise Http404

        return FileResponse(open(module_file.path + "/" + module_file.name, 'rb'))
