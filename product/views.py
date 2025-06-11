from django.shortcuts import render, get_object_or_404
from .models import Product, Category, subCategory
from django.conf import settings
from collections import defaultdict

# Create your views here.
def product_list(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'product/product_list.html', {'products': products, 'MEDIA_URL': settings.MEDIA_URL})

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, is_available=True)
    return render(request, 'product/products_by_category.html', {
        'category': category,
        'products': products
    })

def products_by_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(subCategory, id=subcategory_id)
    products = Product.objects.filter(subcategory=subcategory, is_available=True)
    return render(request, 'product/products_by_subcategory.html', {
        'subcategory': subcategory,
        'products': products
    })
def product_list(request):
    products = Product.objects.select_related('category')
    grouped_products = defaultdict(list)

    for product in products:
        grouped_products[product.category.name].append(product)

    return render(request, 'product/product_list.html', {
        'grouped_products': dict(grouped_products),
    })
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_available=True)
    return render(request, 'product/product_detail.html', {
        'product': product,
        'MEDIA_URL': settings.MEDIA_URL
    })