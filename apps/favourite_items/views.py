from rest_framework import generics
from .serializers import FavouriteItemSerializer
from django.http import JsonResponse
from .models import FavouriteItem


class FavouriteItemList(generics.ListAPIView):

    queryset = FavouriteItem.objects.order_by(
        'created_at').reverse().filter(status='active')
    serializer_class = FavouriteItemSerializer
