from django.views.decorators.http import require_POST
from django.shortcuts import redirect,render,get_object_or_404
from product.models import Product
from django.contrib.auth.decorators import login_required
from.models import Cart, CartItem
from .models import Order, OrderItem
from django.contrib import messages
from django.shortcuts import redirect
from .forms import OrderForm
from django.shortcuts import render
import uuid
from django.http import JsonResponse



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

 
def checkout_view(request):
    return render(request, 'cart/checkout.html')
from django.shortcuts import render
@login_required

# def checkout(request):
#     if request.user.is_authenticated:
#         cart_items = Cart.objects.filter(user=request.user)
#     else:
#         session_key = request.session.session_key
#         if not session_key:
#             request.session.create()
#             session_key = request.session.session_key
#         cart_items = Cart.objects.filter(session_key=session_key)

#     grand_total = sum(item.total_price for item in cart_items)

#     return render(request, 'cart/checkout.html', {
#         'cart_items': cart_items,
#         'grand_total': grand_total
#     }) 


@login_required  
def checkout(request):
    # Get the logged-in user's cart
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()
    grand_total = sum(item.total_price for item in cart_items)
    
    # ✅ Always define form for GET requests
    form = OrderForm()
    
    return render(request, 'cart/checkout.html', {
            'form': form,
            'cart_items': cart_items,
            'grand_total': grand_total
        })
    
    

    # if request.method == "POST":
def checkout_pay(request):
    
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()
    grand_total = sum(item.total_price for item in cart_items)
    
    form = OrderForm(request.POST)
    if form.is_valid():
        # Save the order first
        order = form.save(commit=False)
        order.user = request.user
        order.subtotal = grand_total
        order.total_amount = grand_total
        order.payment_status = "pending"
        order.order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"  
        order.save()
        form.save_m2m()  # <-- Important if OrderForm has ManyToMany fields
        

        # Create related order items
        for item in cart_items:
            OrderItem.objects.create(
            order=order,
            product=item.product,
            product_name=item.product.name,
            product_price=item.product.price,
            quantity=item.quantity,
            )

        # Clear the cart after successful order
        cart.clear()
        return JsonResponse({
            "success": True,
            "order_id": order.id,
            "grand_total": grand_total,
            "message": "Order placed successfully. Proceed to payment."
        })
        
    else:
        messages.error(request, "There was an error with your order. Please try again.")

        # messages.success(request, "Your order has been placed successfully!")

        # checkout_url = (
        # f"https://checkout.oneappgo.com/pay?"
        # f"amount={int(grand_total * 100)}"
        # f"&email={request.user.email}"
        # )
        # return redirect(checkout_url)
            
        
def process_payment(request):
    return render(request, 'cart/payment_success.html') 
 
@login_required
def payment_page(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, "cart/checkout.html", {"order": order})





    # cart, _ = Cart.objects.get_or_create(user=request.user)
    # cart_items = cart.items.all()
    # grand_total = cart.total_price
    # order = None  # default

    # if request.method == "POST":
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         order = form.save(commit=False)
    #         order.user = request.user
    #         order.subtotal = grand_total
    #         order.total_amount = grand_total
    #         order.session_key = request.session.session_key
    #         order.payment_status = "pending"
    #         order.save()

    #         # Save order items
    #         for item in cart_items:
    #             OrderItem.objects.create(
    #                 order=order,
    #                 product=item.product,
    #                 product_name=item.product.name,
    #                 product_price=item.product.price,
    #                 quantity=item.quantity,
    #             )

    #         messages.success(request, "Order created. Proceed to payment.")
    #     else:
    #         print("❌ Form errors:", form.errors)
    # else:
    #     form = OrderForm()

    # return render(request, "cart/checkout.html", {
    #     "form": form,
    #     "cart_items": cart_items,
    #     "grand_total": grand_total,
    #     "order": order,  
    # })

