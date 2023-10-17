# vendors/forms.py

from django import forms
from .models import Vendor

class VendorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Password field for registration

    class Meta:
        model = Vendor
        fields = ['username', 'email', 'password']
