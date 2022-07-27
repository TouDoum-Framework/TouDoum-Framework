from rest_framework import serializers

from modules.example.models.Addr import Addr


class AddrSerializer(serializers.HyperlinkedModelSerializer):
    modules = serializers.HyperlinkedModelSerializer(many=True)

    class Meta:
        model = Addr
        fields = ["url", "ip", "is_private", "scan_priority", "used", "modules", "last_update"]
