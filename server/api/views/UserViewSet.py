from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework import viewsets, permissions

from server.api.views.PermissionViewSet import PermissionSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["url", "username", "first_name", "last_name", "email",
                  "groups", "permissions", "is_staff", "is_active", "date_joined"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
