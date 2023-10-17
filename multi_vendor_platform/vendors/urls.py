# vendors/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register_vendor, name='register_vendor'),
    # Define more URL patterns for product and transaction management
]
