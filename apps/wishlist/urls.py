from django.urls import path
from . import views

urlpatterns = [
    path('', views.WishList.as_view(), name='wish_list'),
    path('add/', views.WishListAdd.as_view(), name='wishlist_add'),
    path('delete/<int:pk>/', views.WishListDelete.as_view(), name='wishlist_delete'),
    path('update/<int:pk>/', views.WishListUpdate.as_view(), name='wishlist_update'),
]
