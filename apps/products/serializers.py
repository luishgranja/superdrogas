from rest_framework import serializers
from .models import Product


class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product
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
