from django.urls import path
from .views import *


urlpatterns = [
    path('submit/', submit_preorder, name='submit_preorder'),
    path('user_preorder/', preorder_history, name='user_preorder'),
    path('customized_gift/', customized_gift_preorder, name='customized_gift_preorder'),
   ]