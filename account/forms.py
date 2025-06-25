from django import forms
from django.contrib.auth.models import User

 
class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name",placeholder="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name" ,placeholder="Last Name")
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.',label="Email",placeholder="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password", placeholder="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password", placeholder="Confirm Password")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password_confirm']

     
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        #check if password match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!") 
        return cleaned_data    
        


 