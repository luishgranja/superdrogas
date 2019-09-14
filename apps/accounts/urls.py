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

from .utilities import get_app_data


ROUTER = routers.DefaultRouter()

ROUTER.register(r'users', UserViewSet)

urlpatterns = [
    url('login/', LoginView.as_view(), name='login'),
    # url('tenant_backup/', get_app_data('public'), name='tenant_backup'),

]

urlpatterns += ROUTER.urls
