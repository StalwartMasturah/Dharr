from django.shortcuts import render
from .models import PreorderRequest
from django.contrib.auth.decorators import login_required
from .forms import PreorderRequestForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import CustomGiftForm

# Create your views here.
@login_required
def submit_preorder(request):
    if request.method == 'POST':
        form = PreorderRequestForm(request.POST, request.FILES)
        if form.is_valid():
            preorder_request = form.save(commit=False)
            preorder_request.user = request.user
            try:
               preorder_request.save()
               messages.info(request, f"Hi{request.user.username},we're checking for {preorder_request.Item_name} and will get back to you soon via email.")
               messages.success(request, "Your preorder request has been submitted successfully.")
            
               return redirect('preorder:preorder_success')
            except Exception as e:
             print(f"Error saving preorder request: {e}")
             messages.error(request, "Oops!Something went wrong while saving your preorder.Please try again.")
    else:
        form = PreorderRequestForm()
    return render(request, 'preorder/submit_preorder.html', {'form': form})

def preorder_history(request):
     preorders = PreorderRequest.objects.filter(user=request.user).order_by('-created_at')
     return render(request, 'preorder/preorder_history.html', {'preorders': preorders})    

def customized_gift_preorder(request):
    if request.method == 'POST':
        form = CustomGiftForm(request.POST, request.FILES)
        if form.is_valid():
            preorder_request = form.save(commit=False)
            preorder_request.user = request.user
            preorder_request.order_type = 'Customized Gift'
            preorder_request.save()
            messages.success(request, "Your customized gift preorder request has been submitted successfully.")
            return redirect('preorder:preorder_success')
    else:
        form = PreorderRequestForm()
    return render(request, 'preorder/customized_gift_preorder.html', {'form': form})