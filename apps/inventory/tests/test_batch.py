"""
Batch test
"""

# Django
from django.test import TestCase

# Inventory models
from apps.inventory.models import (
    Batch,
    Brand,
    Category,
    Product
)


class BatchTestCase(TestCase):
    """
    Batch test

    Validate the CRUD batch actions
    """
    def setUp(self):
        Brand.objects.create(
            name='Bayer',
            email='contacto@bayer.com',
            phone='3157998082'
        )

        Category.objects.create(
            name='Analgesicos',
            description='Medicina general y medicada.'
        )

        Product.objects.create(
            name='Acetaminofen',
            description='Reduce el dolor moderado.',
            price=5000,
            image='http://image/url/path',
            category=Category.objects.get(name='Analgesicos'),
            brand=Brand.objects.get(name='Bayer')
        )

        Batch.objects.create(
            product=Product.objects.get(name='Acetaminofen'),
            quantity=50,
            manufacturing_date='2019-08-21',
            expiration_date='2020-08-21'
        )

    def test_batch_quantity(self):
        """
        All batches save their quantity correctly
        """
        batch = Batch.objects.get(product=Product.objects.get(name='Acetaminofen'))
        self.assertEqual(batch.quantity, 50)
