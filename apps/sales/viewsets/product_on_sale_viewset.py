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
		"""
		Decrease the batch quantity by the purchased amount

		Automatically decrease the batch with the nearest expiration date

		TODO:
			- Correct expiration date
			- Product quantity not suficient or out of stock
		"""

		bought_quantity = serializer.validated_data['quantity']
		batch = Batch.objects.filter(product=serializer.validated_data['product_id']).order_by('expiration_date').first()
		if batch and batch.quantity >= bought_quantity:
			actual_quantity = batch.quantity
			batch.quantity = actual_quantity - bought_quantity
			batch.save(update_fields=['quantity'])
			serializer.save()
		
		

	queryset = ProductOnSaleInvoice.objects.all()
	serializer_class = ProductOnSaleInvoiceSerializer
