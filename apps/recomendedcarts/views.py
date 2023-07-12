from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import RecomendedCartSerializer, RecomendedCartAddSerializer
from ..users.mixins import CustomLoginRequiredMixin
from django_filters.rest_framework import DjangoFilterBackend
from .models import RecomendedCart
from .forms import RecomendedCartForm


class RecomendedCartList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset = RecomendedCart.objects.all()
    serializer_class = RecomendedCartSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user_id']

    def get(self, request, *args, **kwargs):
        self.queryset = RecomendedCart.objects.order_by(
            '-created_at').filter(user=request.login_user)
        return self.list(request, *args, **kwargs)


class RecomendedCartAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset = RecomendedCart.objects.all()
    serializer_class = RecomendedCartAddSerializer

    def post(self, request, *args, **kwargs):
        # Set the user who login
        request.data['user'] = request.login_user.id
        return self.create(request, *args, **kwargs)


class RecomendedCartDelete(CustomLoginRequiredMixin, generics.DestroyAPIView):
    queryset = RecomendedCart.objects.all()
    serializer_class = RecomendedCartSerializer

    def delete(self, request, *args, **kwargs):
        recomendedcart = RecomendedCart.objects.get(pk=self.kwargs['pk'])
        if recomendedcart.user.id != request.login_user.id:
            response = Response(
                {'error': 'You can not delete the cartlist not owned by you.'}, status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            return response
        return self.destroy(request, *args, **kwargs)


class RecomendedCartUpdate(CustomLoginRequiredMixin, generics.UpdateAPIView):
    queryset = RecomendedCart.objects.all()
    serializer_class = RecomendedCartSerializer

    def update(self, request, *args, **kwargs):
        recomendedcart = RecomendedCart.objects.get(pk=self.kwargs['pk'])
        if recomendedcart.user.id != request.login_user.id:
            response = Response(
                {'error': 'You can not update the cartlist not owned by you.'}, status=status.HTTP_404_NOT_FOUND)
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            return response

        recomendedcart.quantity = request.data['quantity']
        recomendedcart.save()
        serializer = RecomendedCartSerializer([recomendedcart], many=True)
        return Response(serializer.data[0])
