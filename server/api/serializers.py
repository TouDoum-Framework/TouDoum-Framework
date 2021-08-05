from rest_framework import serializers

from server.api.models.Addr import Addr
from server.api.models.Config import Config
from server.cluster.models.Master import Master
from server.cluster.models.Worker import Worker
from server.modules.models import Module


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


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    available_at = serializers.StringRelatedField(many=True)

    class Meta:
        model = Module
        fields = ["url", "name", "version", "available_at"]


class MasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Master
        fields = ["url", "uuid", "created_at", "last_update"]


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    current_config = serializers.StringRelatedField(many=True)

    class Meta:
        model = Worker
        fields = ["url", "uuid", "current_config", "created_at"]
