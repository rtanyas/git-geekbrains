# Generated by Django 2.1.1 on 2018-10-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20181021_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcatalog',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена продукта'),
        ),
    ]
