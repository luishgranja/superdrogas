"""
SaleInvoice viewset

Viewset to SaleInvoice serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Sales models
from apps.sales.models.sale_invoice_model import SaleInvoice

# Sales serializers
from apps.sales.serializers.sale_invoice_serializer import SaleInvoiceSerializer


class SaleInvoiceViewSet(viewsets.ModelViewSet):
    """
    SaleInvoice viewset

    CRUD views of the SaleInvoice serializer
    """
    queryset = SaleInvoice.objects.all()
    serializer_class = SaleInvoiceSerializer
