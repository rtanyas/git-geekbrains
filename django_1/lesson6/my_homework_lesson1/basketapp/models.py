from django.db import models
from django.conf import settings
from mainapp.models import Product, ProductCatalog

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket_related_name")
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.ForeignKey(ProductCatalog, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='qty', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)


    #def _get_product_cost(self):
    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.title.price * self.quantity
    
    #product_cost = property(_get_product_cost)
    
    
    #def _get_total_quantity(self):
    @property
    def total_quantity(self):
        "return total quantity for user"
        _items = Basket.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity
        
    #total_quantity = property(_get_total_quantity)
    
    
    #def _get_total_cost(self):
    @property
    def total_cost(self):
        "return total cost for user"
        _items = Basket.objects.filter(user=self.user)
        #_totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost
        
    #total_cost = property(_get_total_cost)
