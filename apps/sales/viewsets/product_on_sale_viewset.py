"""
ProductOnSaleInvoice viewset

Viewset to ProductOnSaleInvoice serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Sales models
from apps.sales.models.product_on_sale_model import ProductOnSaleInvoice

# Sales serializers
from apps.sales.serializers.product_on_sale_serializer import ProductOnSaleInvoiceSerializer


class ProductOnSaleInvoiceViewSet(viewsets.ModelViewSet):
    """
    ProductOnSaleInvoice viewset

    CRUD views of the ProductOnSaleInvoice serializer
    """
    queryset = ProductOnSaleInvoice.objects.all()
    serializer_class = ProductOnSaleInvoiceSerializer