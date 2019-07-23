"""
Products models

Models of the products app
"""

# Django
from django.db import models


class Product(models.Model):
    """
    Product model

    The products offered in the pharmacy
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50)
    sku = models.IntegerField()
    weight = models.IntegerField()
    is_active = models.BooleanField(default=True)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.name
