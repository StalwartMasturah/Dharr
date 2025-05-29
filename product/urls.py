from django.urls import path
from . import views

urlpatterns = [
     
    path('', views.product_list, name='products'),  
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('subcategory/<int:subcategory_id>/', views.products_by_subcategory, name='products_by_subcategory'),
]
 