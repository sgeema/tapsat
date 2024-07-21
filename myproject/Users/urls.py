from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('shop_or_customer/', views.shop_or_customer, name='shop_or_customer'),
    path('add_shoe/', views.add_shoe, name='add_shoe'),
    path('shops/', views.shop_list, name='shop_list'),
    path('shop/<int:pk>/', views.shop_detail, name='shop_detail'),
]
