"""
Batch serializer

Serializer to batch model
"""

# Django Rest Framework
from rest_framework import serializers

# Inventory models
from apps.inventory.models import Batch


class BatchSerializer(serializers.ModelSerializer):
    """
    Batch serializer

    Execute CRUD actions in the batch model
    """
    class Meta:
        model = Batch
        fields = (
            'id',
            'product',
            'product_name',
            'quantity',
            'manufacturing_date',
            'expiration_date',
            'is_active',
        )
