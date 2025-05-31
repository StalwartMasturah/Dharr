
from django.urls import path
from .views import home_view
from .views import *
from . import views

app_name = 'about'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', views.about, name='about'),
 
]
