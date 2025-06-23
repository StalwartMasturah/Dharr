from django.views.decorators.http import require_POST
from django.shortcuts import redirect,render,get_object_or_404
from product.models import Product
from django.contrib.auth.decorators import login_required
from.models import Cart

# Create your views here.

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    grand_total = sum(item.total_price for item in cart_items)

    return render(request, 'cart/cart_list.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'grand_total': grand_total
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')   
 
@require_POST
def update_quantity(request, cart_id):
    action = request.POST.get('action')
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if action == 'increment':
        cart_item.quantity += 1
    elif action == 'decrement' and cart_item.quantity > 1:
        cart_item.quantity -= 1

    cart_item.save()
    return redirect('cart:view_cart')

@require_POST
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('cart:view_cart')
