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
<<<<<<< HEAD
        fields = ('name',
                  'description',
                  'price',
                  'category',
                  'image',
                  'sku',
                  'unit',
                  'weight',
                  'is_active',
                  'brand')
=======
        fields = '__all__'
>>>>>>> 72748a2adfb3a306c9be0a943491a32edd55d104
