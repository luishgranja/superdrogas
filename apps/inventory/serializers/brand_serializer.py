"""
Brand serializer

Serializer to brand model
"""

# Django Rest Framework
from rest_framework import serializers

# Inventory models
from apps.inventory.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """
    Brand serializer

    Execute CRUD actions in the brand model
    """
    class Meta:
        model = Brand
        fields = '__all__'
