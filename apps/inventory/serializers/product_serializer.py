"""
Product serializer

Serializer to product model
"""

# Django Rest Framework
from rest_framework import serializers

# Inventory models
from apps.inventory.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Product serializer

    Execute CRUD actions in the product model
    """
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'image',
            'category',
            'category_name',
            'brand',
            'brand_id',
            'is_active',
        )
