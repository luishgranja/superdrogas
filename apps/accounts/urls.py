"""
Users URLs

The 'urlpatterns' list routes URLs to viewsets
"""

# Django
from django.conf.urls import url

# Django Rest Framework
from rest_framework import routers

# Accounts viewsets
from .viewsets import (
    UserViewSet,
    LoginView
)


ROUTER = routers.DefaultRouter()

ROUTER.register(r'users', UserViewSet)

urlpatterns = [
    url('login/', LoginView.as_view(), name='login')
]

urlpatterns += ROUTER.urls
