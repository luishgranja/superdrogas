"""
Product on sale invoice model

Model to manage products on sale invoice
"""

# Django
from django.db import models

# Sales models
from apps.sales.models.sale_invoice_model import SaleInvoice
# Inventory models
from apps.inventory.models.product_model import Product


class ProductOnSaleInvoice(models.Model):
    """
    ProductOnSaleInvoice model

    """
    sale_invoice_id = models.ForeignKey(SaleInvoice, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product_id.name} {self.quantity}'
