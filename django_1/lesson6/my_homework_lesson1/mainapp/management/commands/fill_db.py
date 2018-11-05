from django.core.management.base import BaseCommand
from mainapp.models import ProductCatalog, Main

import json, os


JSON_PATH = os.path.join('mainapp', 'json')

def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    help = 'Fill DB with new data'

    def handle(self, *args, **options):
        
        Main.objects.all().delete()
		
        authors = loadFromJSON('catalog.json')
        for item in authors:
            new_item = Main(**item)
            new_item.save()
        
                      
        ProductCatalog.objects.all().delete()
		
        products = loadFromJSON('products.json')
        for product in products:
            author_name = product["author"]
            _category = Main.objects.get(author=author_name)
            product['author'] = _category
            new_product = ProductCatalog(**product)
            new_product.save()    

