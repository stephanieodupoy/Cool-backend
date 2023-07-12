from rest_framework import generics
from .serializers import RecomendedItemSerializer
from django.http import JsonResponse
from .models import RecomendedItem


class RecomendedItemList(generics.ListAPIView):
    # Get all posts, limit = 20
    queryset = RecomendedItem.objects.order_by(
        'created_at').reverse().filter(status='active')
    serializer_class = RecomendedItemSerializer
