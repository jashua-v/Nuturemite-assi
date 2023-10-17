from django.shortcuts import render
from .models import Product  # Import your Product model

def homepage(request):
    # Example: Fetch featured products to display on the homepage
    featured_products = Product.objects.filter(is_featured=True)
    context = {
        'featured_products': featured_products
    }
    return render(request, 'homepage.html', context)


def product_page(request):
    # Example: Fetch and display a list of all products
    all_products = Product.objects.all()
    context = {
        'all_products': all_products
    }
    return render(request, 'product_page.html', context)

def vendor_registration(request):
    # Example: Handle vendor registration form submission
    if request.method == 'POST':
        # Create a form for vendor registration and handle form data
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            # Save the vendor registration data to the database
            form.save()
            # You can add authentication or further processing here
    else:
        # If the request method is GET, just render the registration form
        form = VendorRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'vendor_registration.html', context)
