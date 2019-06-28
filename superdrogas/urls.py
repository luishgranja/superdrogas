# Django Rest Framework
from rest_framework import routers

# Apps viewsets
from apps.users.viewsets import UserViewSet
from apps.batch.viewsets import BatchViewSet
from apps.products.viewsets import ProductViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
