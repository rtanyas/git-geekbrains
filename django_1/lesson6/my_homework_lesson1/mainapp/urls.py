from django.urls import path
from mainapp import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'


urlpatterns = [
    path('', views.index_view, name='main'),
    path('catalog/',  views.catalog_view, name='catalog'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('catalog/book/rdmjb/', views.product_rdmjb_view, name='book1'),
    #path('catalog/1/book/1', views.product_view, name='book1'),
    path('catalog/<int:pk>/', views.catalog_view, name='catalog'),
    path('catalog/<int:pk>/page/<page>/', views.catalog_view, name='page')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)