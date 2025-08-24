from django.urls import path
from . views import *

app_name = 'products'

urlpatterns = [
    path('products/', product_list, name='products'),
    path('allproducts/', all_product_list, name='allproducts'),
    path('trending/', trending, name='trending'),
    path('new_arrivals/', new_arrivals, name='new_arrivals'),
    # path('combo_him/', combo_for_him, name='combo_for_him'),
    # path('combo_her/', combo_for_her, name='combo_for_her'), 
    # path('combo_unisex/', combo_unisex, name='combo_unisex'), 
    path('products/<str:category_name>/', filter_by_category, name='filter_by_category'),
    path('products/sub/<str:subcategory_name>/', filter_by_subcategory, name='filter_by_subcategory'),
    path('products/<int:category_id>/', products_by_category, name='products_by_category'),
    path('subcategory/<int:subcategory_id>/', products_by_subcategory, name='products_by_subcategory'),
    path('wishlist/', wishlist_view, name='wishlist'),
    path('wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
 
    
    # path('products/<str:filter_type>/<slug:slug>/', filtered_product_list, name='filtered_products'),

  
 
]
 