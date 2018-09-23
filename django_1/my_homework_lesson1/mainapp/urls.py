from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.index_view),
    path('catalog/',  views.catalog_view),
	path('contacts/', views.contacts_view),
    path('catalog/book/rdmjb/', views.product_rdmjb_view),
    ]