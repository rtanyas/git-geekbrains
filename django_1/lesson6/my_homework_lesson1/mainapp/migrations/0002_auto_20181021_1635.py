# Generated by Django 2.1.1 on 2018-10-21 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCatalog'),
        ),
    ]
