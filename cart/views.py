from django.views.decorators.http import require_POST
from django.shortcuts import redirect,render,get_object_or_404
from product.models import Product
from django.contrib.auth.decorators import login_required
from.models import Cart, CartItem

# Create your views here.
@login_required(login_url='/account/login/')  # redirect to login if not authenticated
def view_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_items = cart.items.all()
    # total_price = sum(item.product.price * item.quantity for item in cart_items)

    grand_total = cart.total_price

    return render(request, 'cart/cart_list.html', {
        'cart_items': cart_items,
        # 'total_price': total_price,
        'grand_total': grand_total
    })
    
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')   
 
@require_POST
def update_quantity(request, cart_id):
    action = request.POST.get('action')
    cart_item = get_object_or_404(CartItem, id=cart_id, cart__user=request.user)

    if action == 'increment':
        cart_item.quantity += 1
    elif action == 'decrement' and cart_item.quantity > 1:
        cart_item.quantity -= 1

    cart_item.save()
    return redirect('cart:view_cart')

@require_POST
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(CartItem, id=cart_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart:view_cart')

from django.shortcuts import render

def checkout_view(request):
    return render(request, 'cart/checkout.html')
from django.shortcuts import render
@login_required

def checkout(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart_items = Cart.objects.filter(session_key=session_key)

    grand_total = sum(item.total_price for item in cart_items)

    return render(request, 'cart/checkout.html', {
        'cart_items': cart_items,
        'grand_total': grand_total
    })

def process_payment(request):
    return render(request, 'cart/payment_success.html')  