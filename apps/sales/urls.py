"""
Sales URLs

The 'urlpatterns' list routes URLs to viewsets
"""

# Django Rest Framework
from rest_framework import routers

# Sales viewsets
from .viewsets.sale_invoice_viewset import SaleInvoiceViewSet
from .viewsets.product_on_sale_viewset import ProductOnSaleInvoiceViewSet

ROUTER = routers.DefaultRouter()

ROUTER.register(r'sales_invoice', SaleInvoiceViewSet)
ROUTER.register(r'product_on_sale', ProductOnSaleInvoiceViewSet)

urlpatterns = ROUTER.urls
