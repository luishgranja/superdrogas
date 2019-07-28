"""
Users URLs

The 'urlpatterns' list routes URLs to viewsets
"""

# Django Rest Framework
from rest_framework import routers

# Accounts viewsets
from .viewsets import UserViewSet


ROUTER = routers.DefaultRouter()

ROUTER.register(r'users', UserViewSet)

urlpatterns = ROUTER.urls
