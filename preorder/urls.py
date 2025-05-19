from django.urls import path
from .views import *

app_name = 'preorder'

urlpatterns = [
    path('submit/', submit_preorder, name='submit'),
    path('history/', preorder_history, name='history'),
    path('gift/', customized_gift_preorder, name='gift'),
    path('detail/<int:id>', preorder_detail, name='detail'),
    path('success/', preorder_success, name='preorder_success'),
    path('self/', preorder_for_self, name='self'),
    path('someone/', preorder_for_someone, name='someone'),


   ]