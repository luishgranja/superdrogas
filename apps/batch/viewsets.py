from rest_framework import viewsets
from .models import Batch
from .serializers import BatchSerialize


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerialize
