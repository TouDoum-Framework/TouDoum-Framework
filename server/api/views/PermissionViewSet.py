from django.contrib.auth.models import Permission

from rest_framework import serializers
from rest_framework import viewsets, permissions


class PermissionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Permission
        fields = ["url", "name", "codename"]


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Permission.objects.all()
        return queryset
