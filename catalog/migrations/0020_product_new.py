# Generated by Django 3.2.25 on 2024-07-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False, help_text='Поставьте галочку, чтобы добавить товар в новинки', verbose_name='Новинка'),
        ),
    ]
