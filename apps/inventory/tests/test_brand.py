"""
Brand test
"""

# Django
from django.test import TestCase

# Inventory models
from apps.inventory.models import Brand


class BrandTestCase(TestCase):
    """
    Brand test

    Validate the CRUD brand actions
    """
    def setUp(self):
        Brand.objects.create(
            name='Bayer',
            email='contacto@bayer.com',
            phone='3157998082'
        )

    def test_brand_email(self):
        """
        All brands save their email correctly
        """
        brand = Brand.objects.get(name='Bayer')
        self.assertEqual(brand.email, 'contacto@bayer.com')
