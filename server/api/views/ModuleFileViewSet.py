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
        if module_name is not None:
            module = Module.objects.filter(name=module_name).first()
            queryset = queryset.filter(module=module)

        file_checksum = self.request.query_params.get("checksum")
        if file_checksum is not None:
            queryset = queryset.filter(checksum=file_checksum)

        is_client = self.request.query_params.get("client")
        if is_client is not None:
            queryset = queryset.filter(is_client=is_client)

        return queryset

    @action(detail=False)
    def download(self, request):
        queryset = self.get_queryset()
        if self.request.query_params.get("checksum") is None or queryset.count() > 1:
            raise Http404

        try:
            module_file: ModuleFile = queryset.get()
            return FileResponse(open(module_file.path + "/" + module_file.name, 'rb'))
        except ModuleFile.DoesNotExist:
            raise Http404
