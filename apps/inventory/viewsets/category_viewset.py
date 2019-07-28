"""
Category viewset

Viewset to category serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Inventory models
from apps.inventory.models import Category

# Inventory serializers
from apps.inventory.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Category viewset

    CRUD views of the category serializer
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()
