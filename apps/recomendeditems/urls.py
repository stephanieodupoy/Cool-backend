from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecomendedItemList.as_view(), name='recomendeditem_list'),
]
