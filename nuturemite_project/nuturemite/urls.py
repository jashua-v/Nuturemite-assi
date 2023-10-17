from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/', views.product_page, name='product_page'),
    path('register/', views.vendor_registration, name='vendor_registration'),
]
