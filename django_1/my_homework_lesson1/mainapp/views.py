from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'mainapp/index.html', {})


def catalog_view(request):
    return render(request, 'mainapp/catalog.html', {})


def contacts_view(request):
    return render(request, 'mainapp/contacts.html', {})


def product_rdmjb_view(request):
    return render(request, 'mainapp/books/rdmjb.html', {})