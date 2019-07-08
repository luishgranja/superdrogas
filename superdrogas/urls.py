"""
URLs configuration

The 'urlpatterns' list routes URLs to views
"""

# Django
from django.conf.urls import url, include

# Django Rest Framework
from rest_framework import routers

# Rest Auth
from rest_auth.views import PasswordResetConfirmView

# Apps viewsets
from apps.users.viewsets import UserViewSet


ROUTER = routers.DefaultRouter()

# CRUD users
ROUTER.register(r'users', UserViewSet)

urlpatterns = ROUTER.urls + [
    url(
        r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    url(r'^rest-auth/', include('rest_auth.urls')),
]
