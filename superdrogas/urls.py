"""
URLs configuration

The 'urlpatterns' list routes URLs to views
"""

# Django
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

# Django Rest Framework
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

# Rest Auth
from rest_auth.views import PasswordResetConfirmView

# Apps viewsets
from apps.users.viewsets import UserViewSet
from apps.batches.viewsets import BatchViewSet
from apps.products.viewsets import ProductViewSet

ROUTER = routers.DefaultRouter()

# CRUD apps
ROUTER.register(r'users', UserViewSet)
ROUTER.register(r'batches', BatchViewSet)
ROUTER.register(r'products', ProductViewSet)

urlpatterns = ROUTER.urls + [
    url(
        r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    url(r'^rest-auth/', include('rest_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

