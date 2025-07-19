from django.shortcuts import render, get_object_or_404
from .models import Product, Category, subCategory,Wishlist
from django.conf import settings
from collections import defaultdict 
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 


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
    
def all_product_list(request):
    wishlist_count = Wishlist.objects.filter(user=request.user).count if request.user.is_authenticated else 0

    #add pagination
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-category')
    # grouped_products = defaultdict(list)

    # get users wishlist
    user_wishlist =[] 
    if request.user.is_authenticated:
        user_wishlist = Wishlist.objects.filter(user=request.user).values_list('added_product_id', flat=True)

    # for product in products:
    #     grouped_products[product.category.name].append(product)
        
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 4)
    
    try:
        top_products = paginator.page(page)
        next_page = int(page) + 1
        prev_page = int(page) - 1
    except PageNotAnInteger:
        top_products = paginator.page(1)
        next_page = 2
        prev_page = 1
        
    except EmptyPage:
        top_products = paginator.page(paginator.num_pages)
        next_page = paginator.num_pages 
        prev_page = paginator.num_pages - 1

    return render(request, 'product/all_product_list.html', {
        'products': top_products,
        'user_wishlist' : list(user_wishlist),
        'next_page': next_page, 'prev_page': prev_page,
        'wishlist_count': wishlist_count,
    })
    
    
def product_list(request):
    products = Product.objects.select_related('category')
    grouped_products = defaultdict(list)
    # get users wishlist
    user_wishlist = []
    wishlist_count = 0
    if request.user.is_authenticated:
        user_wishlist = Wishlist.objects.filter(user=request.user).values_list('added_product_id', flat=True)
        wishlist_count = user_wishlist.count()
     
    for product in products:
        grouped_products[product.category.name].append(product)
        
    return render(request, 'product/product_list.html', {
        'grouped_products': dict(grouped_products),
        'user_wishlist' : list(user_wishlist),
        'wishlist_count': wishlist_count,
    })  
    
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user) if request.user.is_authenticated else []
    print(wishlist_items) 
    wishlist_count = wishlist_items.count()
    return render(request, 'product/wishlist.html', {'wishlist_items': wishlist_items, 'wishlist_count': wishlist_count})


@login_required
def add_to_wishlist(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add to wishlist.")
        return redirect('login')

    try:
        product = Product.objects.get(id=product_id)
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, added_product=product)

        if created:
            messages.success(request, f"{product.name} added to your wishlist.")
        else:
            wishlist_item.delete()
            messages.success(request, f"{product.name} removed from your wishlist.")

    except Product.DoesNotExist:
        messages.error(request, "Product not found.")

    return redirect(request.META.get('HTTP_REFERER', 'products:products'))