"""
Product test
"""

# Django
from django.test import TestCase

# Inventory models
from apps.inventory.models import (
    Brand,
    Category,
    Product
)


class ProductTestCase(TestCase):
    """
    Product test

    Validate the CRUD product actions
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

    def test_product_description(self):
        """
        All products save their description correctly
        """
        product = Product.objects.get(name='Acetaminofen')
        self.assertEqual(product.description, 'Reduce el dolor moderado.')
