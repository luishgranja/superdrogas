"""
Sales URLs

The 'urlpatterns' list routes URLs to viewsets
"""

# Django Rest Framework
from rest_framework import routers

# Sales viewsets
from .viewsets.sale_invoice_viewset import SaleInvoiceViewSet
from .viewsets.product_on_sale_viewset import ProductOnSaleInvoiceViewSet

# Invoices
from .utilities import generar_factura_xml, generar_factura_pdf
from django.conf.urls import url

ROUTER = routers.DefaultRouter()

ROUTER.register(r'sales_invoice', SaleInvoiceViewSet)
ROUTER.register(r'product_on_sale', ProductOnSaleInvoiceViewSet)

urlpatterns = [
    url('xml', generar_factura_xml, name='xml'),
    url('pdf', generar_factura_pdf, name='pdf')
]

urlpatterns += ROUTER.urls
