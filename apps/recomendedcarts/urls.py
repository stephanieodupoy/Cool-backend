from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecomendedCartList.as_view(),
         name='recomendedcart_list'),
    path('recomendedadd/', views.RecomendedCartAdd.as_view(),
         name='recomended_cart_add'),
    path('recomended_delete/<int:pk>/', views.RecomendedCartDelete.as_view(),
         name='recomendedcart_delete'),
    path('recomended_update/<int:pk>/', views.RecomendedCartUpdate.as_view(),
         name='recomendedcart_update'),
]
