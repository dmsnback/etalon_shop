from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Product, ImageProduct


def index(request):
    template = 'catalog/index.html'
    product_list = Product.objects.all()
    image_product = ImageProduct.objects.filter(product=Product())
    context = {
        'product_list': product_list,
        'image_product': image_product
    }
    return render(request, template, context)


def catalog(request):
    template = 'catalog/catalog.html'
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return render(request, template, context)
