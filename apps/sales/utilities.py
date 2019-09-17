"""
Sales utilities
"""

# Django
from django.core import signing
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

# XHTML2PDF
from xhtml2pdf import pisa

# String
from string import Template

# Python
import os

# Sales models
from .models import SaleInvoice, ProductOnSaleInvoice


@csrf_exempt
def generar_factura_xml(request):
    """
    generar_factura_xml
    """
    sale_id = 0

    if request.method == 'GET':
        sale_id = request.GET.get('sale_id')

    sale = SaleInvoice.objects.get(id=sale_id)
    products = ProductOnSaleInvoice.objects.filter(sale_invoice_id=sale_id)

    folder = os.path.dirname(os.path.abspath(__file__))

    invoice_template = os.path.join(folder, 'invoice_template.xml')
    src = Template(open(invoice_template).read())

    product_template_name = os.path.join(folder, 'product.xml')
    src_p = Template(open(product_template_name).read())

    product_list = []

    for product in products:
        data = {
            'id': str(product.product_id),
            'nombre_producto': str(product.product_name()),
            'cantidad': str(product.quantity),
            'iva': f'{product.unit_price * 0.19}',
            'sin_iva': f'{product.unit_price * 0.81}'
        }

        result = src_p.substitute(data)
        product_list.append(result)

    data = {
        # Invoice data
        'prefijo': 'CR',
        'consecutivo': 'CR1',
        'consec_desde': '000000',
        'consec_hasta': '999999',
        'CUFE': signing.dumps(str('hola'), key='3U8A#XFG,,u@Z)', compress=True),

        # Pharmacy data
        'nombre_empresa': 'Super Drogas',
        'NIT': '80526145',
        'departamento_empresa': 'Bogotá DC',
        'ciudad_empresa': 'Bogotá DC',
        'direccion_empresa': 'Cra. 80B 20 - 9',
        'pais_empresa': 'CO',

        # Client data
        'departamento_cliente': 'Valle',
        'ciudad_cliente': 'Cali',
        'direccion_cliente': 'Cll 9 # 4 - El Jordan',
        'pais_cliente': 'CO',
        'nombre_cliente': 'Luis Granja',
        'cedula_cliente': '1144091237',

        # Sale data
        'valor_final': str(sale.total_amount),
        'fecha_compra': str(sale.date),
        'iva': f'{sale.total_amount * 0.19}',
        'sin_iva': f'{sale.total_amount * 0.81}',
        'productos': '\n'.join(product_list)
    }

    result = src.substitute(data)

    response = HttpResponse(result, content_type='text/xml')
    response['Content-Disposition'] = 'attachment'
    response['Content-Disposition'] = 'filename="somefilename.xml"'
    return response


@csrf_exempt
def generar_factura_pdf(request):
    """
    generar_factura_pdf
    """
    sale_id = 0

    if request.method == 'GET':
        sale_id = request.GET.get('sale_id')

    folder = os.path.dirname(os.path.abspath(__file__))

    sale = SaleInvoice.objects.get(id=sale_id)
    products = ProductOnSaleInvoice.objects.filter(sale_invoice_id=sale_id)

    invoice_template = os.path.join(folder, 'invoice_template.html')
    src = Template(open(invoice_template).read())

    product_template_name = os.path.join(folder, 'product.html')
    src_p = Template(open(product_template_name).read())

    product_list = []

    for product in products:
        data = {
            'id': str(product.product_id),
            'nombre_producto': str(product.product_name()),
            'cantidad': str(product.quantity),
            'iva': f'{product.unit_price * 0.19}',
            'sin_iva': f'{product.unit_price * 0.81}',
            'valor_final_producto': str(product.unit_price)
        }

        result = src_p.substitute(data)
        product_list.append(result)

    filename = 'invoice.pdf'
    file = open(filename, "w+b")

    data = {
        # Invoice data
        'prefijo': 'CR',
        'consecutivo': 'CR1',
        'consec_desde': '000000',
        'consec_hasta': '999999',
        'CUFE': signing.dumps(str('hola'), key='3U8A#XFG,,u@Z)', compress=True),

        # Pharmacy data
        'nombre_empresa': 'Super Drogas',
        'NIT': '80526145',
        'departamento_empresa': 'Bogotá DC',
        'ciudad_empresa': 'Bogotá DC',
        'direccion_empresa': 'Cra. 80B 20 - 9',
        'correo_empresa': 'info@adidas.co',
        'telefono_empresa': '32054784',
        'pais_empresa': 'CO',

        # Client data
        'departamento_cliente': 'Valle',
        'ciudad_cliente': 'Cali',
        'direccion_cliente': 'Cll 9 # 4 - El Jordan',
        'pais_cliente': 'CO',
        'nombre_cliente': 'Luis Granja',
        'cedula_cliente': '1144091237',
        'correo_cliente': 'luis@mail.co',
        'telefono_cliente': '32054784',

        # Sale data
        'valor_final': str(sale.total_amount),
        'fecha_compra': str(sale.date),
        'iva': f'{sale.total_amount * 0.19}',
        'sin_iva': f'{sale.total_amount * 0.81}',
        'productos': '\n'.join(product_list)
    }

    result = src.substitute(data)
    pisa_status = pisa.CreatePDF(result, dest=file)

    file.close()

    fs = FileSystemStorage("")
    with fs.open(filename) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        return response
