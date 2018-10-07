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

    path('admin/', admin.site.urls)
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)