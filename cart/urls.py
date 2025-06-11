from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('products/', cart_list, name='cart_list'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', update_quantity, name='update_quantity'),

    # path('checkout/', checkout, name='checkout'),


 

   ]