from rest_framework import serializers

from server.api.models.Addr import Addr
from server.api.models.Config import Config
from server.modules.models import Module, ModuleClientFile


class AddrSerializer(serializers.HyperlinkedModelSerializer):
    modules = serializers.HyperlinkedModelSerializer(many=True)

    class Meta:
        model = Addr
        fields = ["url", "ip", "is_private", "scan_priority", "used", "modules", "last_update"]


class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    modules_enabled = serializers.StringRelatedField(many=True)

    class Meta:
        model = Config
        fields = ["url", "pause", "modules_enabled", "timeout", "created_at"]


class ModuleClientFileSerializer(serializers.HyperlinkedModelSerializer):
    module = serializers.StringRelatedField(many=True)

    class Meta:
        model = ModuleClientFile
        fields = ["name", "hash", "module"]


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    depend_on = serializers.StringRelatedField(many=True)

    class Meta:
        model = Module
        fields = ["url", "name", "display_name", "description", "version", "depend_on", "author", "repo"]
