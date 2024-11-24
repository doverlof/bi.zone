from rest_framework import serializers
from .models import Subnet
import ipaddress


class SubnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnet
        fields = ["id", "subnet", "company_id", "created_at"]

    def validate_subnet(self, value):
        try:
            ipaddress.IPv4Network(value, strict=False)
        except ValueError:
            raise serializers.ValidationError(
                "Введите корректное значение IP-адреса с маской в формате CIDR"
            )
        return value
