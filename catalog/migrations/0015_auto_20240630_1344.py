# Generated by Django 3.2.25 on 2024-06-30 13:44

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20240630_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproduct',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите изображение товара', upload_to=catalog.models.upload_path_product, verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=catalog.models.upload_path_product),
        ),
    ]
