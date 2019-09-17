"""
User model

Model to manage users in the application
"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model

    Extend from Django's Abstract User
    """

    ROLES = [
        ('AD', 'Administrator'),
        ('CM', 'Customer'),
        ('SL', 'Seller'),
    ]

    identification_number = models.CharField(max_length=10, unique=True)
    rol = models.CharField(max_length=2, choices=ROLES)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

    def rol_name(self):
        """
        rol_name return user rol
        """
        return self.get_rol_display()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone']
