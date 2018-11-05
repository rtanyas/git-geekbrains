from django.shortcuts import render
from mainapp.models import ProductCatalog, Product, Main
from basketapp.models import Basket
from django.shortcuts import render, get_object_or_404
import random, os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def _get_hot_product(products):
    #products = ProductCatalog.objects.all()
    return random.sample(list(products), 1)[0]


def _get_same_products(hot_product):
    return ProductCatalog.objects.filter(author=hot_product.author).exclude(pk=hot_product.pk)[:2]


def _basket(user):
#def _basket(request):
    if user.is_authenticated:
    #if request.user.is_authenticated:        
        #print('-----------sql basket-----------:', basket.query)
        #print('-----------queryset basket-----------:', basket)
        #return Basket.objects.filter(user=request.user)
    #return Basket.objects.filter(user=user)
        return user.basket_related_name.all()
    #return request.user.basket_related_name.all()
    return []

# Create your views here.
def index_view(request):
    title = "home"
    #basket = _basket(request)
    basket = _basket(request.user)
    authors = Main.objects.all()

    content = {'title': title, 'authors': authors, 'basket': basket}
        
    return render(request, os.path.join('mainapp', 'index.html'), content)


#def catalog_view(request, pk=None):
def catalog_view(request, pk=None, page=1):
    links_menu = Main.objects.all()
    print('-----------catalog pk-----------:', pk, type(pk))
    basket = _basket(request.user)
    hot_product = []

    caption = "All books"
    if pk:        
        if pk == '0':
            books = ProductCatalog.objects.all().order_by('title')
            #author = Main.objects.all()
            
        else:
            author = get_object_or_404(Main, pk=pk)
            caption = author
            books = ProductCatalog.objects.filter(author__pk=pk).order_by('title')
    else:
        books = ProductCatalog.objects.all().order_by('title')
        #author = Main.objects.all()
    hot_product = _get_hot_product(books)
    same_products = _get_same_products(hot_product)

    # экземпляр класса Paginator 1- сколько объектов на странице
    paginator = Paginator(books, 1)
    try:
        # получение объектов нужной сраницы
        products_paginator = paginator.page(page)
        print(type(products_paginator))
    except PageNotAnInteger:
        # если передано в качестве страницы не число, то первая страница
        products_paginator = paginator.page(1)
    except EmptyPage:
        # если переданная страница слишком большее число, то последняя страница
        products_paginator = paginator.page(paginator.num_pages)

    print('---------type_of_books>', type(books))
    print('---------type_of_products_paginator>', type(products_paginator))
 
    content = {
            #'title': author,
            "caption": caption,            
            'links_menu': links_menu,
            #'author': author,
            ###'books': books,
            'books': products_paginator,
            'basket': basket,
            'hot_product': hot_product,
            'same_products': same_products,
        }
    print('-----------sql catalog-----------:', books.query)
    
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
    return render(request, os.path.join('mainapp', 'catalog.html'), content)


def contacts_view(request):
    title = "contact us"
    basket = _basket(request.user)
    content = {'title': title, 'basket': basket}
    return render(request, os.path.join('mainapp', 'contacts.html'), content)


def product_rdmjb_view(request):
    title = "Roald Dahl"
    #title = Product.objects.all()
    basket = _basket(request.user)
    return render(request, 'mainapp/books/rdmjb.html', {'title': title, 'basket': basket})

def product_view(request, pk):
    caption = "Roald Dahl"
    basket = _basket(request.user)
    #title = Product.objects.all()  

    if pk:
        #if pk == '0':
        #    book = Product.objects.all().order_by('title')
        #    #author = Main.objects.all()
        #    
        #else:
        #    #author = get_object_or_404(Main, pk=pk)
        #    #caption = author
        book = Product.objects.filter(title__pk=pk)
        #print("book!!!!!!!!!!", book)
        #print('-----------book pk-----------:', pk, type(pk))
    #else:
    book = Product.objects.all().order_by('title')
    #book = get_object_or_404(Product, pk=pk)
    #author = Main.objects.all()

    content = {
        'caption': caption,
        'book': book,
        'basket': basket,
        'links_menu': Main.objects.all()}
    return render(request, os.path.join('mainapp', 'books', 'dahl1.html'), content)