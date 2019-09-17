# Django Tenants
from django_tenants.utils import schema_context

# Django
from django.http import JsonResponse
from django.db.models import Sum
from apps.sales.models.product_on_sale_model import ProductOnSaleInvoice
from apps.inventory.models.product_model import Product


def get_products_report(request):
    if request.method == 'GET':
        schema_name = request.GET.get('schema_name')

    response = {}
    nombres = []
    cantidades = []

    with schema_context(schema_name):
        products = ProductOnSaleInvoice.objects.all().values('product_id').annotate(counter=Sum('quantity')). \
                   order_by('-counter')[:5]

        for product in products:
            product_name = Product.objects.get(id=product['product_id']).name
            cantidad = product['counter']
            nombres.append(product_name)
            cantidades.append(cantidad)
        response.update({'nombres': '|'.join(nombres), 'cantidad': ','.join(cantidades)})

    return JsonResponse(response)