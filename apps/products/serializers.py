"""
Products serializers

Serializers of the products app
"""

# Django Rest Framework
from rest_framework import serializers

# Products models
from .models import Product


class ProductSerialize(serializers.ModelSerializer):
    """
    Products serializer

    For execute the CRUD actions in the product model
    """
    class Meta:
        model = Product
        fields = '__all__'
