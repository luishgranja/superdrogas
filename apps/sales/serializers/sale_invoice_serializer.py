"""
SaleInvoice serializer

Serializer to SaleInvoice model
"""

# Django Rest Framework
from rest_framework import serializers

# Sales models
from apps.sales.models.sale_invoice_model import SaleInvoice


class SaleInvoiceSerializer(serializers.ModelSerializer):
    """
    SaleInvoice serializer

    Execute CRUD actions in the SaleInvoice model
    """
    class Meta:
        model = SaleInvoice
        fields = (
            'id',
            'user_id',
            'client_id',
            'sale_type',
            'date',
            'total_amount'
        )
