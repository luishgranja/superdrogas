"""
Sales utilities
"""

# String
from string import Template

# Django
from django.core import signing
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


# XHTML2PDF
from xhtml2pdf import pisa

import os


def generar_factura_xml(request):

    if request.method == 'GET':
        print(request.GET)

    """
    generar_factura_xml
    """
    folder = os.path.dirname(os.path.abspath(__file__))

    invoice_template = os.path.join(folder, 'invoice_template.xml')

    # template_name = r'invoice_template.xml'
    src = Template(open(invoice_template).read())

    # product_template_name = 'product.xml'
    product_template_name = os.path.join(folder, 'product.xml')
    src_p = Template(open(product_template_name).read())
    product_list = []
    products = ['a']

    for _ in products:
        data = {
            'nombre_producto': 'Doloran',
            'id': '1',
            'cantidad': '2',
            'iva': f'{25000 * 0.19}',
            'sin_iva': f'{25000 * 0.81}',
        }

        result = src_p.substitute(data)
        product_list.append(result)

    # filename = f'{name}.xml'
    # file = open(filename, "w+")

    data = {
        # Invoice data
        'prefijo': 'CR',
        'consecutivo': 'CR1',
        'consec_desde': '000000',
        'consec_hasta': '999999',
        'CUFE': signing.dumps(str('hola'), key='3U8A#XFG,,u@Z)', compress=True),

        # Pharmacy data
        'nombre_empresa': 'Adidas Co.',
        'NIT': '80526145',
        'departamento_empresa': 'DC',
        'ciudad_empresa': 'Bogotá',
        'direccion_empresa': 'Cra 80B 20-9',
        'pais_empresa': 'CO',

        # Client data
        'departamento_cliente': 'VAC',
        'ciudad_cliente': 'Cali',
        'direccion_cliente': 'El Jordan calle 25',
        'pais_cliente': 'CO',
        'nombre_cliente': 'Luis Granja',
        'cedula_cliente': '1144091237',

        # Sale data
        'valor_final': '25000',
        'fecha_compra': '2019-12-15',
        'iva': f'{25000*0.19}',
        'sin_iva': f'{25000*0.81}',
        'productos': '\n'.join(product_list),

        # Crypto data
    }

    result = src.substitute(data)

    # file.write(result)
    response = HttpResponse(result, content_type='text/xml')
    response['Content-Disposition'] = 'attachment'
    response['Content-Disposition'] = 'filename="somefilename.xml"'
    return response
    # file.close()


def generar_factura_pdf(request):
    """
    generar_factura_pdf
    """

    folder = os.path.dirname(os.path.abspath(__file__))

    invoice_template = os.path.join(folder, 'invoice_template.html')
    product_template_name = os.path.join(folder, 'product.html')
    # template_name = 'invoice_template.html'
    src = Template(open(invoice_template).read())

    # product_template_name = 'product.html'
    src_p = Template(open(product_template_name).read())
    product_list = []
    products = ['a']

    for _ in products:
        data = {
            'nombre_producto': 'Doloran',
            'id': '1',
            'cantidad': '2',
            'sin_iva': f'{2* 25000 * 0.81}',
            'valor_final_producto': f'{2* 25000 * 0.81}',
        }

        result = src_p.substitute(data)
        product_list.append(result)

    name = 'hola'

    filename = f'{name}.pdf'
    file = open(filename, "w+b")

    data = {
        # Invoice data
        'consecutivo': 'CR1',

        # Pharmacy data
        'nombre_empresa': 'Adidas Co.',
        'NIT': '80526145',
        'departamento_empresa': 'DC',
        'ciudad_empresa': 'Bogotá',
        'direccion_empresa': 'Cra 80B 20-9',
        'correo_empresa': 'info@adidas.co',
        'telefono_empresa': '32054784',

        # Client data
        'departamento_cliente': 'VAC',
        'ciudad_cliente': 'Cali',
        'direccion_cliente': 'El Jordan calle 25',
        'nombre_cliente': 'Luis Granja',
        'cedula_cliente': '1144091237',
        'correo_cliente': 'luis@mail.co',
        'telefono_cliente': '32054784',

        # Sale data
        'valor_final': '25000',
        'fecha_compra': '2019-12-15',
        'iva': f'{25000 * 0.19}',
        'sin_iva': f'{25000 * 0.81}',
        'productos': ''.join(product_list),

        # Crypto data
    }

    result = src.substitute(data)
    pisa_status = pisa.CreatePDF(result, dest=file)

    # file.close()

    fs = FileSystemStorage("/")
    with fs.open(filename) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="'+filename+'"'
        return response


