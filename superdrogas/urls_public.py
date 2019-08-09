"""
URL configuration for public scheme

The 'urlpatterns' list routes URLs to views
"""

# Django
from django.conf.urls import url, include

# Rest Auth
from rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    # Project apps
    url('', include('apps.pharmacies.urls')),
    url('accounts/', include('apps.accounts.urls')),

    # Rest Auth
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^rest-auth/', include('rest_auth.urls')),
]
