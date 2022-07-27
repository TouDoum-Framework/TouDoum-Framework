from rest_framework import serializers

from server.api.models.Config import Config
from server.modules.models import Module, ModuleFile


class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    modules_enabled = serializers.StringRelatedField(many=True)

    class Meta:
        model = Config
        fields = ["url", "pause", "modules_enabled", "timeout", "created_at"]


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    depend_on = serializers.StringRelatedField(many=True)

    class Meta:
        model = Module
        fields = ["url", "name", "display_name", "description", "version", "depend_on", "author", "repo"]


class ModuleFileSerializer(serializers.HyperlinkedModelSerializer):
    module = serializers.StringRelatedField(many=False)

    class Meta:
        model = ModuleFile
        fields = ["url", "name", "path", "checksum", "module", "is_client"]
