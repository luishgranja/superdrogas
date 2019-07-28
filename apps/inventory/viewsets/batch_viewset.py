"""
Batch viewset

Viewset to batch serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Inventory models
from apps.inventory.models import Batch

# Inventory serializers
from apps.inventory.serializers import BatchSerializer


class BatchViewSet(viewsets.ModelViewSet):
    """
    Batch viewset

    CRUD views of the batch serializer
    """
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()
