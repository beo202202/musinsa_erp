from django.urls import path
from . import views


# erp/urls.py
urlpatterns = [
    path('product-create/', views.product_create, name='product_create'),
    path('product-list/', views.product_list, name='product_list'),
    path('product-success/', views.product_success, name='product_success'),
    path('product-all-delete/', views.product_all_delete,
         name='product_all_delete'),
    path('product-my-all-delete/', views.product_my_all_delete,
         name='product_my_all_delete'),
    path('inbound-create/', views.inbound_create, name='inbound_create'),
    path('outbound/<str:product_id>/',
         views.outbound_create, name='outbound_create'),
    path('inventory/', views.inventory, name='inventory'),
]
