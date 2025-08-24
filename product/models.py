from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name
     
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    description = models.TextField(blank=True)
    details = models.TextField(blank=True)
    default_image = models.ImageField(upload_to='product_images/')
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    added_product = models.ForeignKey(Product, related_name='wishlist_items', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'added_product')  # Ensures one product per user
        ordering = ['-added_on']

    def __str__(self):
        return f"{self.user.username} - {self.added_product.name}"
 