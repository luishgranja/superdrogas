"""
Inventory URLs

The 'urlpatterns' list routes URLs to viewsets
"""

# Django Rest Framework
from rest_framework import routers

# Inventory viewsets
from .viewsets import PharmacyViewSet


ROUTER = routers.DefaultRouter()

ROUTER.register(r'pharmacies', PharmacyViewSet)

urlpatterns = ROUTER.urls
