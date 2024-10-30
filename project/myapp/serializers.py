# myapp/serializers.py
from rest_framework import serializers
from .models import Subnet


class SubnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnet
        fields = ["id", "subnet", "company_id", "created_at"]
