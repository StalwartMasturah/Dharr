from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "order_for",
            "recipient_name",
            "recipient_phone",
            "recipient_address_line1",
            "recipient_address_line2",
            "recipient_city",
            "recipient_state",
            "recipient_postal_code",
            "recipient_country",
            "customer_name",
            "customer_email",
            "customer_phone",
            "order_notes",
        ]
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"}),
            "customer_email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "customer_phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "order_for": forms.Select(attrs={"class": "form-control"}),
            "recipient_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Recipient’s Name"}),
            "recipient_phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Recipient’s Phone"}),
            "recipient_address_line1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Street Address"}),
            "recipient_address_line2": forms.TextInput(attrs={"class": "form-control", "placeholder": "Address Line 1"}),
            "recipient_city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "recipient_state": forms.TextInput(attrs={"class": "form-control", "placeholder": "State"}),
            "recipient_postal_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Postal Code"}),
            "recipient_country": forms.TextInput(attrs={"class": "form-control", "placeholder": "Country"}),
            "order_notes": forms.Textarea(attrs={"class": "form-control", "placeholder": "Any special notes?", "rows": 3}),
        }
    def clean_customer_phone(self):
        phone = self.cleaned_data.get("customer_phone")
        if not phone.isdigit():
            raise forms.ValidationError("Phone number should contain only digits.")
        if len(phone) != 11:
            raise forms.ValidationError("Phone number must be exactly 11 digits.")
        return phone

    # Recipient phone validation
    def clean_recipient_phone(self):
        phone = self.cleaned_data.get("recipient_phone")
        if phone:  # recipient phone may be optional
            if not phone.isdigit():
                raise forms.ValidationError("Recipient phone should contain only digits.")
            if len(phone) != 11:
                raise forms.ValidationError("Recipient phone must be exactly 11 digits.")
        return phone
