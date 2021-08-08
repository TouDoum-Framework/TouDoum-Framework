from django.http import Http404
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from server.api.models.Config import Config, get_last_config
from server.api.serializers import ConfigSerializer


class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all().order_by("id")
    serializer_class = ConfigSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False)
    def latest(self, request):
        config = get_last_config()
        if config is not None:
            serializer = self.get_serializer(config)
            return Response(serializer.data)
        raise Http404
