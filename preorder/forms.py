from django import forms
from .models import PreorderRequest
  

class PreorderRequestForm(forms.ModelForm):
    class Meta:
        model = PreorderRequest
        fields = ['Item_name', 'description', 'item_image', 'address', 'city', 'state', 'zip_code']
        labels = {
            'Item_name': 'Item Name',
            'description': 'Description',
            'item_image': 'Item Image',
            'address': 'Delivery Address',
            'city': 'City',
            'state': 'State',
            'zip_code': 'Zip Code', 
        }
        widgets = {
            'Item_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your desired item name'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter a brief description of the item'}),
            'item_image': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder': 'Upload an image of the item'}),
            'address': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter delivery address'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the city'}),
            'state': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the state'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '6-digit ZIP code'}),

 
         }
class CustomGiftForm(forms.ModelForm):
    class Meta:
        model = PreorderRequest
        fields = ['Item_name', 'description', 'item_image', 'address', 'city', 'state', 'zip_code']
        labels = {
            'Item_name': 'Item Name',
            'description': 'Description',
            'item_image': 'Item Image',
            'address': 'Delivery Address',
            'city': 'City',
            'state': 'State',
            'zip_code': 'Zip Code',
            
        }
        widgets = {
            'Item_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your desired item name'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter a brief description of the item'}),
            'item_image': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder': 'Upload an image of the item'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter delivery address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the state'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '6-digit ZIP code'}),
        }

class PreorderRequestFormSomeone(forms.ModelForm):
    class Meta:
        model = PreorderRequest
        fields = ['Item_name', 'description', 'item_image', 'recipient_name', 'recipient_address', 'recipient_city', 'recipient_phone', 'recipient_zip_code','custom_message']
        labels = {
            'Item_name': 'Item Name',
            'description': 'Description',
            'item_image': 'Item Image',
             # New recipient fields
            'recipient_name': "Recipient's Name",
            'recipient_address': "Recipient's Address",
            'recipient_city': "Recipient's City",
            'recipient_phone': "Recipient's Phone Number",
            'recipient_zip_code': "Recipient's Zip Code",
            'custom_message': "Custom Message",
        }
        widgets = {
            # Existing fields
            'Item_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your desired item name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief description of the item'}),
            'item_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Upload an image of the item'}),
            'recipient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter recipient's name"}),
            'recipient_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter recipient's address"}),
            'recipient_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter recipient's city"}),
            'recipient_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter recipient's phone number"}),
            'recipient_zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '6-digit ZIP code'}),
            'custom_message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter a custom message for the recipient if you want us to add a note to their order"}),
        }
            
            # New recipient fields
            # Add widgets for new recipient fields if needed
        