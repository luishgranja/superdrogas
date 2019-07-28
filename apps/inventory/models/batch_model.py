"""
Batch model

Model to manage batches of products in stock
"""

# Django
from django.db import models

# Inventory models
from .product_model import Product


class Batch(models.Model):
    """
    Batch model

    A batch of a product is used to describe the
    quantities of a product in the inventory
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    manufacturing_date = models.DateField()
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product.name} {self.quantity}'

    def product_name(self):
        """
        product_name return the name of the brand product
        """
        return self.product.name
