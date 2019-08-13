from django.shortcuts import render
from .models import Product

def product_list(request):
    context ={
        'product_list':Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)

def category(request):
    context = {
        'current_category': None,
        'product_list': None,
    }
    return render(request, 'catalog/category.html')

