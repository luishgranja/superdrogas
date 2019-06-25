"""
URLs configuration

The 'urlpatterns' list routes URLs to views
"""

# Django
from django.conf.urls import url

# Django Rest Framework
from rest_framework import routers

# Apps viewsets
from apps.users.viewsets import UserViewSet, ChangePasswordView


ROUTER = routers.DefaultRouter()

# CRUD users
ROUTER.register(r'users', UserViewSet)

urlpatterns = ROUTER.urls + [
    url(r'change-password', ChangePasswordView.as_view())
]
