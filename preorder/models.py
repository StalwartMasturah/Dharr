from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PreorderRequest(models.Model):
    ORDER_TYPES = [
        ('self ', 'For Yourself'),
        ('gift', 'For a Gift'),
        ('gift', 'Customized Gift')
        ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Availabe', 'Available'),
        ('Not Available', 'Not Available'),
        ('Awaiting Payment', 'Awaiting Payment'),
        ('In Progress', 'In Progress'),
        ('Awaiting Shipment', 'Awaiting Shipment'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('On Hold', 'On Hold'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_type= models.CharField(max_length=50, choices=ORDER_TYPES, default='self')
    Item_name = models.CharField(max_length= 50)
    description = models.TextField(blank=True)
    item_image = models.ImageField(upload_to='preorder_images/', height_field=None, width_field=None, max_length=None,blank=True, null=True) 
    status = models.CharField(max_length=50, default='Pending') 
    delivery_address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return f"{self.user.username} wants to preorder {self.Item_name}"



def status_message(self):
    name = self.user.first_name
    if self.status == 'Pending':
        return f"Hi {name}, Your preorder request for {self.Item_name} is pending."
    elif self.status == 'Available':
        return f"Hi {name}, Your preorder request for {self.Item_name} is available."
    elif self.status == 'Not Available':
        return f"Hi {name}, Your preorder request for {self.Item_name} is not available."
    elif self.status == 'Awaiting Payment':
        return f"Hi {name}, Your preorder request for {self.Item_name} is awaiting payment."
    elif self.status == 'In Progress':
        return f"Hi {name}, Your preorder request for {self.Item_name} is in progress."
    elif self.status == 'Awaiting Shipment':
        return f"Hi {name}, Your preorder request for {self.Item_name} is awaiting shipment."
    elif self.status == 'Shipped':
        return f"Hi {name}, Your preorder request for {self.Item_name} has been shipped."
    elif self.status == 'Delivered':
        return f"Hi {name}, Your preorder request for {self.Item_name} has been delivered."
    elif self.status == 'Completed':
        return f"Hi {name}, Your preorder request for {self.Item_name} has been completed."
    elif self.status == 'Cancelled':
        return f"Hi {name}, Your preorder request for {self.Item_name} has been cancelled."
    elif self.status == 'On Hold':
        return f"Hi {name}, Your preorder request for {self.Item_name} is on hold."
    else:
        return f"Hi {name}, Your preorder request for {self.Item_name} has an unknown status."
    
    
    
class PreorderRequestComment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.preorder_request.Item_name}"
    