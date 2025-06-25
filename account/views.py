 # To handle views and redirect
from django.shortcuts import render, redirect
# To import auth functions from Django
from django.contrib.auth import authenticate, login, logout
# the login required decorator to protect views
from django.contrib.auth.decorators import login_required 
# for cbv ( class based view)
from django.contrib.auth.mixins import LoginRequiredMixin
#For CBV
from django.views import View
#Import user class (model)
from django.contrib.auth.models import User
# import the RegisterForm from forms.py
from .forms import RegisterForm
from django import forms

# Register View

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Extract form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                password_confirm=password_confirm,
                first_name=first_name,
                last_name=last_name
            )
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Log the user in and redirect
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {'form': form})

# Login View
# This view handles both GET and POST requests for user login.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
            return render(request, 'accounts/login.html', {'error': error_message})
    
    # Handle GET requests (i.e., first time loading the page)
    return render(request, 'accounts/login.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')
    
# Home View
# UIng the decorator
@login_required
def home_view(request):
    return render(request, 'auth1_app/home.html')

#Protected view 
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # next to redirect url
    redirect_field_name = 'redirect'
     
    def get(self, request):
        return render(request, 'registration/protected.html')
    
    
        
        

    
 