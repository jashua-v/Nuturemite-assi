# vendors/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Vendor(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

# Add related_name to the 'groups' and 'user_permissions' fields
Vendor._meta.get_field('groups').remote_field.related_name = 'vendor_groups'
Vendor._meta.get_field('user_permissions').remote_field.related_name = 'vendor_user_permissions'
