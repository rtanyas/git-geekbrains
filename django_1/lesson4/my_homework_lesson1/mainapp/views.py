from django.shortcuts import render
from .models import ProductCatalog, Product, Main

# Create your views here.
def index_view(request):
    title = "home"
    authors = Main.objects.all()
    return render(request, 'mainapp/index.html', {'title': title, 'authors': authors})


def catalog_view(request):
    title = "catalog"
    books = ProductCatalog.objects.all()
    
    #books = [{"description": "Roald Dahl's Marvellous Joke Book is full of jokes, limericks, riddles",
    #          "url_name": "Roald Dahl's Marvellous Joke Book",
    #          "title": "Marvellous Joke Book",
    #          "alt": "book_cover",
    #          "image_file": "RDMJB.jpg"},
    #         {"description": "Book #2 description.",
    #          "url_name": "Book #2",
    #          "title": "Book #2",
    #          "alt": "book_cover",
    #          "image_file": "RDMJB.jpg"}]
    return render(request, 'mainapp/catalog.html', {'title': title, 'books': books})


def contacts_view(request):
    title = "contact us"
    return render(request, 'mainapp/contacts.html', {'title': title})


def product_rdmjb_view(request):
    title = "Roald Dahl"
    #title = Product.objects.all()
    return render(request, 'mainapp/books/rdmjb.html', {'title': title})