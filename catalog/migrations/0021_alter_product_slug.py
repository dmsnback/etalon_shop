# Generated by Django 3.2.25 on 2024-07-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_product_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='Ссылка'),
        ),
    ]