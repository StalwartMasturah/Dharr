from django.contrib import admin
from .models import *

# Register your models here.

class CartItemInline(admin.TabularInline):  
    model = CartItem
    extra = 0
    
class OrderInline(admin.StackedInline):
    model = Order
    extra = 0
    max_num = 1  # Only one order per cart
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    
admin.site.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "session_key", "created_at", "updated_at", "total_items", "total_price")
    inlines = [CartItemInline, OrderInline]

   
admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_amount", "is_paid", "paid_at")
    readonly_fields = ("description",)  # 👈 makes description read-only
    list_filter = ("is_paid",)
    inlines = [OrderItemInline]


admin.site.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity", "total_price", "added_at", "updated_at")
    list_filter = ("cart", "product")
    search_fields = ("product__name", "cart__user__username")
    
    
admin.site.register(OrderItem) 