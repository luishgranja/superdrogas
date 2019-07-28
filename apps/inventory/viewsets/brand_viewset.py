"""
Brand viewset

Viewset to brand serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Inventory models
from apps.inventory.models import Brand

# Inventory serializers
from apps.inventory.serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    """
    Brand viewset

    CRUD views of the brand serializer
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()
