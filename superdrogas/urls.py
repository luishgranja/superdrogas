# Django Rest Framework
from rest_framework import routers
from django.conf.urls import url


# Apps viewsets
from apps.users.viewsets import UserViewSet, ChangePasswordView

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)

# Change password url definition
url_password = url(r'change-password', ChangePasswordView.as_view())

urlpatterns = router.urls + [url_password]
