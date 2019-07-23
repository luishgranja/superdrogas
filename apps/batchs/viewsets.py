"""
Batches viewsets

Viewsets and views of the batches app
"""

# Django Rest Framework
from rest_framework import viewsets

# Batches models
from .models import Batch

# Batches serializers
from .serializers import BatchSerialize


class BatchViewSet(viewsets.ModelViewSet):
    """
    Batch viewset

    To define the CRUD views of the batch model
    """
    queryset = Batch.objects.all()
    serializer_class = BatchSerialize

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()
