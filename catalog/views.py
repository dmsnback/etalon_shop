from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Product, ImageProduct


def index(request):
    template = 'catalog/index.html'
    product_list = Product.objects.all()
    image_product = ImageProduct.objects.all()
    context = {
        'product_list': product_list,
        'image_product': image_product
    }
    return render(request, template, context)
