from django.conf.urls import url
from django.urls import path

from basketapp import views

app_name = 'basketapp'

urlpatterns = [
    path('', views.basket, name='view'),
    path('add/<int:pk>/', views.add_product_to_basket, name='add_item_to_basket'),
    path('delete/<int:pk>/', views.remove_product_from_basket, name='remove_item_from_basket'),
    
]