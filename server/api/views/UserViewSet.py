from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework import viewsets, permissions

from server.api.views.PermissionViewSet import PermissionSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["url", "username", "first_name", "last_name", "email", "password", "groups", "permissions",
                  "is_staff", "is_active", "date_joined"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def save(self, **kwargs):
        user = super().save(**kwargs)
        password = self.validated_data.get('password', None)
        if password:
            user.set_password(password)
            user.save()
        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.all().order_by("pk")
        return queryset
