"""
Inventory URLs

The 'urlpatterns' list routes URLs to viewsets
"""

# Django Rest Framework
from rest_framework import routers

# Inventory viewsets
from .viewsets import (
    BatchViewSet,
    BrandViewSet,
    CategoryViewSet,
    ProductViewSet,
)


app_name = 'inventory'

ROUTER = routers.DefaultRouter()

ROUTER.register(r'batches', BatchViewSet)
ROUTER.register(r'brands', BrandViewSet)
ROUTER.register(r'categories', CategoryViewSet)
ROUTER.register(r'products', ProductViewSet)

urlpatterns = ROUTER.urls
