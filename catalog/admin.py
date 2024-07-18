from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from catalog.models import (
    Category,
    ColorProduct,
    Favorite,
    LocationProduct,
    Product,
    ImageProduct
)


class CustomMPTTModelAdmin(DjangoMpttAdmin):
    mptt_level_indent = 30
    list_display = (
        'name',
        'parent',
    )
    list_display_links = (
        'name',
    )
    list_filter = ('name', 'parent')
    search_fields = ('name',)
    expand_tree_by_default = True


class ColorProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)
    empty_value_display = 'Не задано'


class LocationProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    list_display_links = ('name',)
    empty_value_display = 'Не задано'


class ImageProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')


class ImageProductInline(admin.TabularInline):
    fk_name = 'product'
    model = ImageProduct


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageProductInline,]
    list_display = (
        'title',
        'article',
        'price',
        'new',
        'image',
        'location_product',
        'color',
        'volume',
        'category',
        'description',
        'composition',
        'usage'

    )
    search_fields = (
        'title',
        'article',
        'new'
        'location_product',
        'color',
        'volume',
        'category',
        'composition',

    )
    list_filter = (
        'title',
        'article',
        'new',
        'location_product',
        'color',
        'volume',
        'category',
        'composition',
    )


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product'
    )


admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(ColorProduct, ColorProductAdmin)
admin.site.register(LocationProduct, LocationProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ImageProduct, ImageProductAdmin)
admin.site.register(Favorite, FavoriteAdmin)

