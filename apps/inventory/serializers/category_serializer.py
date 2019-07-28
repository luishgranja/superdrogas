"""
Category serializer

Serializer to category model
"""

# Django Rest Framework
from rest_framework import serializers

# Inventory models
from apps.inventory.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Category serializer

    Execute CRUD actions in the category model
    """
    class Meta:
        model = Category
        fields = '__all__'
