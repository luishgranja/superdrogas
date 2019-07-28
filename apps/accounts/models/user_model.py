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
    identification_number = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firt_name', 'last_name', 'email', 'phone']
