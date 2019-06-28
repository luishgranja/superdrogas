from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50)
    sku = models.IntegerField()
    unit = models.IntegerField()
    weight = models.IntegerField()
    is_active = models.BooleanField()
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.name
