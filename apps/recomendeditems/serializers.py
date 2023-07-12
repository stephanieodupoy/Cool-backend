from .models import RecomendedItem
from rest_framework import serializers


class RecomendedItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = RecomendedItem
        fields = '__all__'
