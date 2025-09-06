from django.db import models
from product.models import Product
from django.conf import settings
from decimal import Decimal
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='cart')
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, blank=True)
    # quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_items(self):
        """Total number of items in cart"""
        return sum(item.quantity for item in self.items.all())
    
    @property
    def total_price(self):
        """Total price of all items in cart"""
        return sum(item.total_price for item in self.items.all())
    
    @property
    def is_empty(self):
        """Check if cart is empty"""
        return not self.items.exists()
    
    def clear(self):
        """Remove all items from cart"""
        self.items.all().delete()
    
    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        # return f"Cart for session {self.session_key}"
        
class CartItem(models.Model):
    """CartItem model - individual products in a cart with quantities
    """
    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('cart', 'product')  # One product per cart
        ordering = ['-added_at']
    
    @property
    def total_price(self):
        """Total price for this cart item"""
        if self.product.price:
            return self.product.price * self.quantity
        return Decimal('0.00')
    
    @property
    def is_in_stock(self):
        """Check if requested quantity is available"""
        return self.product.stock >= self.quantity
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity} in cart"
    
    
# order (with addrss), orderitem
# Order models for checkout 
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    order_for = models.CharField(
        max_length=20, 
        choices=[("self", "Myself"), ("someone", "Someone else")],
        default="self"
    )
    recipient_name = models.CharField(max_length=100, blank=True, null=True)
    recipient_phone = models.CharField(max_length=20, blank=True, null=True)
    recipient_address = models.TextField(blank=True, null=True)
    recipient_address_line1 = models.CharField(max_length=200)
    recipient_address_line2 = models.CharField(max_length=200, blank=True, null=True)   
    recipient_city = models.CharField(max_length=100)
    recipient_state = models.CharField(max_length=100)
    recipient_postal_code = models.CharField(max_length=20)
    recipient_country = models.CharField(max_length=100)
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    description = models.TextField(blank=True, null=True)  
    order_number = models.CharField(max_length=20, unique=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20, blank=True)
    
    payment_method = models.CharField(max_length=50, blank=True)
    payment_reference = models.CharField(max_length=100, blank=True)
    
    order_notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.order_number} by {self.user.username} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"

 
    
    class Meta:
        ordering = ['-created_at']
    
def save(self, *args, **kwargs):
       if not self.order_number:
        self.order_number = self.generate_order_number()
        lines = []
        total = 0

       if self.pk:  # only if order already exists
        for item in self.items.all():
            line_total = item.total_price
            total += line_total
            lines.append(
                f"{item.product} | Qty: {item.quantity} | "
                f"Price: {item.product_price} | Total: {line_total}"
            )

       if lines:
        lines.append(f"Grand Total: {total}")
        self.description = "\n".join(lines)

    # Always save
       super().save(*args, **kwargs)

def generate_order_number(self):
        import random, string
        from django.utils import timezone
        date_str = timezone.now().strftime('%Y%m%d')
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        return f"ORD-{date_str}-{random_str}"
    
@property
def total_items(self):
        return sum(item.quantity for item in self.items.all())
    
def __str__(self):
        return f"Order {self.order_number} - {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)  
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['id']
    
    @property
    def total_price(self):
        return self.product_price * self.quantity
    
    def __str__(self):
        return f"{self.product_name} x {self.quantity} in order {self.order.order_number}"
    
