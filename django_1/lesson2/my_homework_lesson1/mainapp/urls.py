from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.index_view, name='main'),
    path('catalog/',  views.catalog_view, name='catalog'),
	path('contacts/', views.contacts_view, name='contacts'),
    path('catalog/book/rdmjb/', views.product_rdmjb_view, name='book1'),
    ]