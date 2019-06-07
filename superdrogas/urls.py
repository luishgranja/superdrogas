# Django Rest Framework
from rest_framework import routers

# Apps viewsets
from apps.users.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = router.urls
