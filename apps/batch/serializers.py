"""
Batches serializers

Serializers of the batches app
"""

# Django Rest Framework
from rest_framework import serializers

# Batches models
from .models import Batch


class BatchSerialize(serializers.ModelSerializer):
    """
    Batches serializer

    For execute the CRUD actions in the batch model
    """
    class Meta:
        model = Batch
        fields = ('id', 'product', 'quantity', 'manufacturing_date', 'expiration_date', 'is_active', 'NombreProducto')
