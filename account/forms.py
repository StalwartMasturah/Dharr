from django import forms
from django.contrib.auth.models import User

 
class RegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=150, required=True,widget=forms.TextInput(attrs={'placeholder': 'FullName'}))
    email = forms.EmailField(max_length=254,required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email','required': 'required'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password'}))
    password_confirm = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Password','type':'password'}))

    class Meta:
        model = User
        fields = ['name','email', 'password', 'password_confirm']

     
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        #check if password match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!") 
        return cleaned_data    
        


 