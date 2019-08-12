"""
ProductOnSaleInvoice viewset

Viewset to ProductOnSaleInvoice serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Sales models
from apps.sales.models.product_on_sale_model import ProductOnSaleInvoice
from apps.inventory.models.batch_model import Batch

# Sales serializers
from apps.sales.serializers.product_on_sale_serializer import ProductOnSaleInvoiceSerializer


class ProductOnSaleInvoiceViewSet(viewsets.ModelViewSet):
    """
    ProductOnSaleInvoice viewset

    CRUD views of the ProductOnSaleInvoice serializer
    """

    def perform_create(self, serializer):
        bought_quantity = serializer.validated_data['quantity']
        batch = Batch.objects.get(product=serializer.validated_data['product_id'])
        actual_quantity = batch.quantity
        batch.quantity = actual_quantity - bought_quantity
        batch.save(update_fields=['quantity'])

        serializer.save()

    queryset = ProductOnSaleInvoice.objects.all()
    serializer_class = ProductOnSaleInvoiceSerializer
