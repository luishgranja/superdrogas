from django.db import models
from apps.products.models import Product

class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    manufacturing_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return self.product
