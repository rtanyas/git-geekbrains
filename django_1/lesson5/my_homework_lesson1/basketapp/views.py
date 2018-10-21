from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product, ProductCatalog


def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('title__author')
    content = {'title': title, 'basket_items': basket_items}
    return render(request, 'basketapp/basket.html', content)

    
def add_product_to_basket(request, pk):
    print('-----------pk_basket-----------:', pk)
    product = get_object_or_404(Product, pk=pk)
    print('-----------product_basket-----------:', product)
    #product = get_object_or_404(ProductCatalog, pk=pk)
    old_basket_item = Basket.objects.filter(user=request.user, title=product)
    
    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
        print('-----------old_basket_item[0].quantity-----------:', old_basket_item[0].quantity)
    else:
        new_basket_item = Basket(user=request.user, title=product)
        new_basket_item.quantity += 1
        new_basket_item.save()
        print('-----------new_basket_item.quantity-----------:', new_basket_item.quantity)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
def remove_product_from_basket(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    