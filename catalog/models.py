from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


User = get_user_model()


def upload_path_product(instance, filename):
    return ('catalog/{0}/{1}/{2}').format(
        instance.category.name,
        instance.title, filename
    )


class Category(MPTTModel):
    """Модель категорий"""

    name = models.CharField(
        'Категория',
        max_length=128,
        unique=True,
        help_text='Название категории'
    )
    slug = models.SlugField(
        max_length=64,
        unique=True
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Главная категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name = 'Категория',
        verbose_name_plural = 'Категории'
        ordering = ('id',)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'catalog:product_list_by_category',
            kwargs={'category_slug': self.slug}
        )


class LocationProduct(models.Model):
    """Модель страны производителя"""

    name = models.CharField(
        'Название страны',
        max_length=128,
        help_text='Укажите стрвну'
    )

    class Meta:
        verbose_name = 'Название страны'
        verbose_name_plural = 'Название стран'

    def __str__(self):
        return self.name


class ColorProduct(models.Model):
    """Модель цвета товара"""

    name = models.CharField(
        'Цвет товара',
        max_length=128,
        help_text='Укажите цвет'
    )

    class Meta:
        verbose_name = 'Цвет товара'
        verbose_name_plural = 'Цвета товаров'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Категория',
    )
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Укажите название товара'
    )
    slug = models.SlugField(
        'Ссылка',
        max_length=64,
        unique=True,
        help_text='Добавте уникальную ссылку'
    )
    location_product = models.ForeignKey(
        LocationProduct,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    article = models.CharField(
        'Артикул товара',
        max_length=64,
        unique=True,
        help_text='Добавте уникальный артикул товара'
    )
    description = models.TextField(
        'Описание',
        blank=True,
        help_text='Добавте описание'
    )
    color = models.ForeignKey(
        ColorProduct,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    image = models.ImageField(
        'Фото товара',
        upload_to=upload_path_product,
        blank=True
    )
    volume = models.IntegerField(
        'Объём товара',
        blank=True,
        null=True,
        help_text='Укажите объём товара'
    )
    composition = models.TextField(
        'Состав товара',
        blank=True,
        help_text='Укажите состав товара'
    )
    usage = models.TextField(
        'Использование товара',
        blank=True,
        help_text='Укажите использование товара'
    )
    price = models.DecimalField(
        'Цена',
        max_digits=10,
        decimal_places=2,
        help_text='Укажите цену'
    )

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        verbose_name = 'Товар',
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class ImageProduct(models.Model):
    """Модель изображений"""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='images'
    )
    image = models.ImageField(
        'Изображение товара',
        upload_to=upload_path_product,
        blank=True,
        help_text='Загрузите изображение товара'
    )

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'

    def __str__(self):
        return self.product.title
