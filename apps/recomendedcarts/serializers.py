from rest_framework.generics import ListCreateAPIView
from .models import RecomendedCart
from rest_framework import serializers


class RecomendedCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecomendedCart
        fields = '__all__'
        depth = 1


class RecomendedCartAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecomendedCart
        fields = '__all__'
