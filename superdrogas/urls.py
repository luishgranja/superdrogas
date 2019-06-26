"""
URLs configuration

The 'urlpatterns' list routes URLs to views
"""

# Django
from django.conf.urls import url, include
from django.views.generic import TemplateView

# Django Rest Framework
from rest_auth.views import PasswordResetConfirmView, PasswordResetView
from rest_framework import routers

# Apps viewsets
from apps.users.viewsets import UserViewSet


ROUTER = routers.DefaultRouter()

# CRUD users
ROUTER.register(r'users', UserViewSet)

urlpatterns = ROUTER.urls + [
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(),  name='password_reset_confirm'),

]
