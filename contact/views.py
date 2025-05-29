from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"From: {name} <{email}>\n\n{message}"

            send_mail(subject, full_message, email, ['dharrincense@gmail.com'])  
            messages.success(request, 'Your message has been sent. Thank you!')
            form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

