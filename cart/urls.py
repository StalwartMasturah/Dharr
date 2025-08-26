from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
    path('', view_cart, name='view_cart'), 
    path('update/<int:cart_id>/', update_quantity, name='update_quantity'),  
    path('remove/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('process-payment/', process_payment, name='process_payment'),
    path("payment/<int:order_id>/", payment_page, name="payment_page"),
    path("payment-success/", process_payment, name="payment_success"),
    



] 
    
     

    # path('checkout/', checkout, name='checkout'),


 