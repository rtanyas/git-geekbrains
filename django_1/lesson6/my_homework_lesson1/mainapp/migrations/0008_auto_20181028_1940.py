# Generated by Django 2.1.1 on 2018-10-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20181028_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcatalog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creation_date'),
        ),
        migrations.AlterField(
            model_name='productcatalog',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='price'),
        ),
    ]
