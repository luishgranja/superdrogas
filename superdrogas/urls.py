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
<<<<<<< HEAD
from apps.batch.viewsets import BatchViewSet
=======
from apps.batchs.viewsets import BatchViewSet
>>>>>>> 72748a2adfb3a306c9be0a943491a32edd55d104
from apps.products.viewsets import ProductViewSet


<<<<<<< HEAD
router.register(r'users', UserViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
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
>>>>>>> 72748a2adfb3a306c9be0a943491a32edd55d104
