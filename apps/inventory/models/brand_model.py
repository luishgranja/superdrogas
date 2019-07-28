"""
Brand model

Model to manage product suppliers
"""

# Django
from django.db import models


class Brand(models.Model):
    """
    Brand model

    A brand is a supplier or manufacturer of products
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
