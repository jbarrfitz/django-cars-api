from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "make", "model", "year")
        model = Car
