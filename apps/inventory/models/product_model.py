"""
Product model

Model to manage products in the pharmacy
"""

# Django
from django.db import models

# Inventory models
from .category_model import Category
from .brand_model import Brand


class Product(models.Model):
    """
    Product model

    A product is an item for sale
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def category_name(self):
        """
        category_name return the name of the product category
        """
        return self.category.name

    def brand_name(self):
        """
        brand_name return the name of the product brand
        """
        return self.brand.name
