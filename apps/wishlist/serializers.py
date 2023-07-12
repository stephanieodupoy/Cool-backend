from rest_framework.generics import ListCreateAPIView
from .models import Wish
from rest_framework import serializers


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'
        depth = 1


class WishlistAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'
