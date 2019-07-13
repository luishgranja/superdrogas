"""
Batches models

Models of the batches app
"""

# Django
from django.db import models

# Batches models
from apps.products.models import Product


class Batch(models.Model):
    """
    Batch model

    Batch of a product, used to describe the quantities
    of a product in inventory
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    manufacturing_date = models.DateField()
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product
