from django.db import models
from product.models import Product
from django.conf import settings
from decimal import Decimal


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='cart')
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
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
    """
    CartItem model - individual products in a cart with quantities
    """
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

    
    
    

