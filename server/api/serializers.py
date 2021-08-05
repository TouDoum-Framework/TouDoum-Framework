from django.contrib.auth.models import User
from rest_framework import serializers

from server.api.models.Addr import Addr
from server.api.models.Config import Config
from server.modules.models import Module


class AddrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Addr
        fields = ["url", "ip", "isPrivate", "rescanPriority", "used", "lastUpdate"]


class ConfigSerializer(serializers.HyperlinkedModelSerializer):

    modulesEnabled = serializers.StringRelatedField(many=True)

    class Meta:
        model = Config
        fields = ["url", "pause", "modulesEnabled", "timeout", "createdAt"]


class ModulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Module
        fields = ["url", "name", "version"]
