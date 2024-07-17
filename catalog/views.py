from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Product, ImageProduct
from catalog.utils import get_page_context

def index(request):
    template = 'catalog/index.html'
    product_list = Product.objects.all()
    image_product = ImageProduct.objects.filter(product=Product())
    category_list = Category.objects.all()
    context = {
        'product_list': product_list,
        'image_product': image_product,
        'category_list': category_list,

    }
    return render(request, template, context)


def catalog(request):
    template = 'catalog/shop.html'
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    page_obj = get_page_context(product_list, request)
    context = {
        'product_list': product_list,
        'category_list': category_list,
        'page_obj': page_obj
    }
    return render(request, template, context)


def detail_product(request, slug):
    template = 'catalog/detail.html'
    product = get_object_or_404(
        Product.objects.all(), slug=slug)
    category_list = Category.objects.all()
    context = {
        'product': product,
        'category_list': category_list
    }
    return render(request, template, context)
