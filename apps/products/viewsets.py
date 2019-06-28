from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerialize


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialize
