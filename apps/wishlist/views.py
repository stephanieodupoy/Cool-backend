from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import WishlistSerializer, WishlistAddSerializer
from ..users.mixins import CustomLoginRequiredMixin
from django_filters.rest_framework import DjangoFilterBackend
from .models import Wish
from .forms import WishListForm


class WishList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishlistSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user_id']

    def get(self, request, *args, **kwargs):
        self.queryset = Wish.objects.order_by(
            '-created_at').filter(user=request.login_user)
        return self.list(request, *args, **kwargs)


class WishListAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishlistAddSerializer

    def post(self, request, *args, **kwargs):
        # Set the user who login
        request.data['user'] = request.login_user.id
        return self.create(request, *args, **kwargs)


class WishListDelete(CustomLoginRequiredMixin, generics.DestroyAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishlistSerializer

    def delete(self, request, *args, **kwargs):
        wishlist = Wish.objects.get(pk=self.kwargs['pk'])
        if wishlist.user.id != request.login_user.id:
            response = Response(
                {'error': 'You can not delete the cartlist not owned by you.'}, status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            return response
        return self.destroy(request, *args, **kwargs)


class WishListUpdate(CustomLoginRequiredMixin, generics.UpdateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishlistSerializer

    def update(self, request, *args, **kwargs):
        wishlist = Wish.objects.get(pk=self.kwargs['pk'])
        if wishlist.user.id != request.login_user.id:
            response = Response(
                {'error': 'You can not update the cartlist not owned by you.'}, status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            return response

        wishlist.quantity = request.data['quantity']
        wishlist.save()
        serializer = WishlistSerializer([wishlist], many=True)
        return Response(serializer.data[0])
