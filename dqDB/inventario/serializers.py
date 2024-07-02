from rest_framework import serializers
from .models import IceCream


class IceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        field = '__all__'