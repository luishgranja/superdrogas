"""
Category viewset

Viewset to category serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Inventory models
from apps.inventory.models import Category
import requests
# Inventory serializers
from apps.inventory.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Category viewset

    CRUD views of the category serializer
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()

    def perform_create(self, serializer):
        category = serializer.save()
        payload = 'v=1&t=pageview&tid=UA-148049900-1&cid=c76c5a95-406f-4ed8-8c59-096da9f0cc36'
        r = requests.post('http://www.google-analytics.com/collect', data=payload)
        print (r)

