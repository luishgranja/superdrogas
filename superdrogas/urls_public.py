"""
URL configuration for public scheme

The 'urlpatterns' list routes URLs to views
"""

# Django
from django.conf.urls import url, include

# Rest Auth
from rest_auth.views import PasswordResetConfirmView

# Vue project
from .views import vue


urlpatterns = [
    # Project apps
    url('api/', include('apps.pharmacies.urls')),
    url('api/accounts/', include('apps.accounts.urls')),

    # Rest Auth
    url(r'^api/password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^api/rest-auth/', include('rest_auth.urls')),

    # Vue project
    url(r'^.*$', vue, name='vue'),
]
