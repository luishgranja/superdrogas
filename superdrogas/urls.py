# Django Rest Framework
from rest_framework import routers

# Apps viewsets
from apps.users.viewsets import UserViewSet
from apps.batch.viewsets import BatchViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'batches', BatchViewSet)

urlpatterns = router.urls
