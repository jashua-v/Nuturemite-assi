# vendors/views.py

from django.shortcuts import render, redirect
from .forms import VendorRegistrationForm
from django.contrib import messages
from django.contrib.auth import login

def register_vendor(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            vendor = form.save()
            login(request, vendor)  # Log in the newly registered vendor
            messages.success(request, 'Vendor registration successful!')
            return redirect('dashboard')  # Implement the dashboard view
    else:
        form = VendorRegistrationForm()
    return render(request, 'register_vendor.html', {'form': form})


def homepage(request):
    return render(request, 'homepage.html')
