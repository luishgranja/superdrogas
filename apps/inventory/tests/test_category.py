"""
Category test
"""

# Django
from django.test import TestCase

# Inventory models
from apps.inventory.models import Category


class CategoryTestCase(TestCase):
    """
    Category test

    Validate the CRUD category actions
    """
    def setUp(self):
        Category.objects.create(name='Medicamentos', description='Medicina general y medicada.')

    def test_category_description(self):
        """
        All categories save their description correctly
        """
        medicamentos = Category.objects.get(name='Medicamentos')
        self.assertEqual(medicamentos.description, 'Medicina general y medicada.')
