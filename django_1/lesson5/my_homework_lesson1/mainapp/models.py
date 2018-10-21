from django.db import models


class Main(models.Model):
    author = models.CharField(verbose_name='имя автора', max_length=128)
    description = models.CharField(verbose_name='краткое описание автора', max_length=60, blank=True)
    #author_foto = models.ImageField(upload_to='authors_images', blank=True)

    def __str__(self):
        return self.author


class ProductCatalog(models.Model):
    author = models.ForeignKey(Main, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='название продукта', max_length=128)
    url_name = models.CharField(verbose_name='название ссылки продукта', max_length=128)
    image_file = models.ImageField(upload_to='books_images', blank=True)
    description = models.CharField(verbose_name='краткое описание продукта', max_length=255, blank=True)
    alt = models.CharField(verbose_name='значение alt для тега img', max_length=128, default="book_cover")
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    
    def __str__(self):
        return self.title

    
class Product(models.Model):
    title = models.ForeignKey(ProductCatalog, on_delete=models.CASCADE)
    #title = models.CharField(verbose_name='название продукта', max_length=64, unique=True)
    
    def __str__(self):
        return self.title 
