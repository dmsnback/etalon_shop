from django.shortcuts import render

from catalog.models import Category


def about(request):
    template = 'pages/about.html'
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return render(request, template, context)


def contact(request):
    template = 'pages/contact.html'
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return render(request, template, context)
