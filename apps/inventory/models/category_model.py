"""
Category model

Model to manage product categories.
"""

# Django
from django.db import models


class Category(models.Model):
    """
    Category model

    A category is a type that allows you to group products
    """
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
