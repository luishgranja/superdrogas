# Django Rest Framework
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

# Apps viewsets
from apps.users.viewsets import UserViewSet
from apps.batch.viewsets import BatchViewSet
from apps.products.viewsets import ProductViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
