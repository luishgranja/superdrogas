from django.db import models


class Batch(models.Model):
    product = models.CharField(max_length=20)
    quantity = models.IntegerField()
    manufacturing_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return self.product
