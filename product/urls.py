from django.urls import path
from . views import *

app_name = 'products'

urlpatterns = [
    path('products/', product_list, name='products'),
    path('allproducts/', all_product_list, name='allproducts'),
    path('products/<int:category_id>/', products_by_category, name='products_by_category'),
    path('wishlist/', wishlist_view, name='wishlist'),
    path('wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    # path('products/<str:filter_type>/<slug:slug>/', filtered_product_list, name='filtered_products'),

  
 
]
 