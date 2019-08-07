"""
Category client test
"""

# Django Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Inventory models
from apps.inventory.models import Category


class TestCategoryClient(APITestCase):
    """
    Category client test
    """
    def setUp(self):
        Category.objects.create(
            id=1,
            name='Medicamentos',
            description='Medicina general y medicada.'
        )
        self.data = {'name': 'Analgesico', 'description': 'Reduce el dolor.'}

    def test_create_category(self):
        """
        Issue a POST request
        """
        response = self.client.post('/inventory/categories/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_categories(self):
        """
        Issue a GET request
        """
        response = self.client.get('/inventory/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category(self):
        """
        Issue a GET request
        """
        response = self.client.get('/inventory/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            (response.data['name'], response.data['is_active']),
            ('Medicamentos', True)
        )
