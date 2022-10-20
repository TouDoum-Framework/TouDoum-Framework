from django.contrib.auth.models import Group

from rest_framework import serializers
from rest_framework import viewsets, permissions

from server.api.views.PermissionViewSet import PermissionSerializer


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ["id", "url", "name", "permissions"]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("pk")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Group.objects.all()
        return queryset
