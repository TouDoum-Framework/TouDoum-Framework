from django.contrib.auth.models import User
from rest_framework import serializers

from server.api.models.Addr import Addr


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class AddrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Addr
        fields = ["url", "ip", "isPrivate", "rescanPriority", "used", "lastUpdate"]
