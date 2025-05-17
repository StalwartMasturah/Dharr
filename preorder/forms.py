from django import forms
from .models import PreorderRequest


class PreorderRequestForm(forms.ModelForm):
    class Meta:
        model = PreorderRequest
        fields = ['Item_name', 'description', 'item_image', 'delivery_address']
        labels = {
            'Item_name': 'Item Name',
            'description': 'Description',
            'item_image': 'Item Image',
            'delivery_address': 'Delivery Address',
        }
        widgets = {
            'Item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'item_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control'}),
        }
class CustomGiftForm(forms.ModelForm):
    class Meta:
        model = PreorderRequest
        fields = ['Item_name', 'description', 'item_image', 'delivery_address']
        labels = {
            'Item_name': 'Item Name',
            'description': 'Description',
            'item_image': 'Item Image',
            'delivery_address': 'Delivery Address',
        }
        widgets = {
            'Item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'item_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control'}),
        }