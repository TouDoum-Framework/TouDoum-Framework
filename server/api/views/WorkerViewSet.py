from rest_framework import viewsets, permissions

from server.api.serializers import WorkerSerializer
from server.cluster.models.Worker import Worker


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all().order_by("id")
    serializer_class = WorkerSerializer
    permission_classes = [permissions.IsAuthenticated]
