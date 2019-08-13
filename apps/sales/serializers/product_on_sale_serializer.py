"""
ProductOnSaleInvoice serializer

Serializer to ProductOnSaleInvoice model
"""

# Django Rest Framework
from rest_framework import serializers

# Sales models
from apps.sales.models.product_on_sale_model import ProductOnSaleInvoice


class ProductOnSaleInvoiceSerializer(serializers.ModelSerializer):
    """
    ProductOnSaleInvoice serializer

    Execute CRUD actions in the ProductOnSaleInvoice model
    """
    class Meta:
        model = ProductOnSaleInvoice
        fields = (
            'sale_invoice_id',
            'product_id',
            'product_name',
            'product_description',
            'product_subtotal',
            'quantity',
            'total_price',
            'is_active',
        )
