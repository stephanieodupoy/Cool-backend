from .models import FavouriteItem
from rest_framework import serializers


class FavouriteItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = FavouriteItem
        fields = '__all__'
