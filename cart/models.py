from django.db import models
from product.models import Product
from django.conf import settings


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_price(self):
        if self.product.price:
            return self.product.price * self.quantity
        return 0
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
    
    

