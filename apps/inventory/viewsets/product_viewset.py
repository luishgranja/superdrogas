"""
Product viewset

Viewset to product serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Inventory models
from apps.inventory.models import Product

# Inventory serializers
from apps.inventory.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product viewset

    CRUD views of the product serializer
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()
