from django.urls import path
from . import views

urlpatterns = [
    path('', views.FavouriteItemList.as_view(), name='favouriteitem_list'),
]
