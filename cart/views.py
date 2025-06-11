from django.shortcuts import redirect,render, get_object_or_404
from product.models import Product

# Create your views here.
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', '/'))
 
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

def cart_list(request):
    cart = request.session.get('cart', {})  # Format: {product_id: quantity}
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            item_total = product.price * quantity
            total_price += item_total

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
            })
        except Product.DoesNotExist:
            continue  # Skip if product doesn't exist

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/cart_list.html', context)

def update_quantity(request, item_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if str(item_id) in cart:
            if action == 'increase':
                cart[str(item_id)] = cart.get(str(item_id), 1) + 1
            elif action == 'decrease' and cart[str(item_id)] > 1:
                cart[str(item_id)] -= 1
            elif quantity > 0:
                cart[str(item_id)] = quantity

        request.session['cart'] = cart
    return redirect('cart:cart_list')
