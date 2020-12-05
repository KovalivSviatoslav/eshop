from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Product


# Create your views here.
def product_search(request):
    """Пошук по сайту"""
    search_query = request.GET['search']
    search_response = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query), is_active=True)
    if not search_response:
        search_response = Product.objects.filter(is_active=True)
    return search_response

def products_list(request):
    """Список всіх товарів або список товарів за пошуком"""
    search_key = 'search'
    if search_key in request.GET:
        # Був виконаний пошук по сайту.
        products = product_search(request)
    else:
        products = Product.objects.filter(is_active=True)
    context = {
        'products': products,
    }
    return render(request, 'products/products_list.html', context=context)


def product_detail(request, slug):
    """Сторінка конкретного товару"""
    product = Product.objects.get(slug__iexact=slug)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context=context)

def products_category(request, slug):
    """Список всіх товарів в категорії"""
    products = Product.objects.filter(Q(categories__parent__slug__iexact=slug) | Q(categories__slug__iexact=slug), is_active=True)
    context = {
        'products': products
    }
    return render(request, 'products/products_list.html', context=context)