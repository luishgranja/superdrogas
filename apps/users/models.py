"""
Users models

Models of the users app
"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    """
    User model

    Extend from Django's Abstract User
    """
    username = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']
