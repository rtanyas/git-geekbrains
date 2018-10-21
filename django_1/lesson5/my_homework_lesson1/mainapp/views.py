from django.shortcuts import render
from mainapp.models import ProductCatalog, Product, Main
from basketapp.models import Basket
from django.shortcuts import render, get_object_or_404


def _basket(request):
    basket = []
    if request.user.is_authenticated:
        #basket = Basket.objects.filter(user=request.user)
        basket = request.user.basket_related_name.all()
        print('-----------sql basket-----------:', basket.query)
        print('-----------queryset basket-----------:', basket)
        return basket


# Create your views here.
def index_view(request):
    title = "home"
    basket = _basket(request)
    authors = Main.objects.all()

    content = {'title': title, 'authors': authors, 'basket': basket}
        
    return render(request, 'mainapp/index.html', content)


def catalog_view(request, pk=None):
    links_menu = Main.objects.all()
    print('-----------pk-----------:', pk, type(pk))
    basket = _basket(request)

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

    content = {
            #'title': author,
            "caption": caption,            
            'links_menu': links_menu,
            #'author': author,
            'books': books,
            'basket': basket,
        }
    
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
    return render(request, 'mainapp/catalog.html', content)


def contacts_view(request):
    title = "contact us"
    basket = _basket(request)
    content = {'title': title, 'basket': basket}
    return render(request, 'mainapp/contacts.html', content)


def product_rdmjb_view(request):
    title = "Roald Dahl"
    #title = Product.objects.all()
    return render(request, 'mainapp/books/rdmjb.html', {'title': title})


