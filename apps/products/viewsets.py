"""
Products viewsets

Viewsets and views of the products app
"""

# Django Rest Framework
from rest_framework import viewsets

# Products models
from .models import Product

# Products serializers
from .serializers import ProductSerialize


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product viewset

    To define the CRUD views of the product model
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerialize

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()
