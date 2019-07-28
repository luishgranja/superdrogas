"""
URLs configuration

The 'urlpatterns' list routes URLs to views
"""

# Django
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

# Rest Auth
from rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    # Project apps
    url('inventory/', include('apps.inventory.urls')),
    url('accounts/', include('apps.accounts.urls')),

    # Rest Auth
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^rest-auth/', include('rest_auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
