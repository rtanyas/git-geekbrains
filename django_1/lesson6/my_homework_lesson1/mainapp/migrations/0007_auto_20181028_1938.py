# Generated by Django 2.1.1 on 2018-10-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20181028_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcatalog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='productcatalog',
            name='edited',
            field=models.DateTimeField(auto_now=True, verbose_name='дата редактирования'),
        ),
    ]