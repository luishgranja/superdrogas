from string import Template
from django.core import signing
from xhtml2pdf import pisa


def generar_factura_xml(name):
    template_name = 'invoice_template.xml'
    src = Template(open(template_name).read())

    product_template_name = 'product.xml'
    src_p = Template(open(product_template_name).read())
    product_list = []
    products = ['a']

    for product in products:
        data = {
            'nombre_producto': 'Doloran',
            'id': '1',
            'cantidad': '2',
            'iva': f'{25000 * 0.19}',
            'sin_iva': f'{25000 * 0.81}',
        }

        result = src_p.substitute(data)
        product_list.append(result)

    filename = f'{name}.xml'
    file = open(filename, "w+")

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

    file.write(result)
    file.close()


def generar_factura_pdf(name):
    template_name = 'invoice_template.html'
    src = Template(open(template_name).read())

    product_template_name = 'product.html'
    src_p = Template(open(product_template_name).read())
    product_list = []
    products = ['a']

    for product in products:
        data = {
            'nombre_producto': 'Doloran',
            'id': '1',
            'cantidad': '2',
            'sin_iva': f'{2* 25000 * 0.81}',
            'valor_final_producto': f'{2* 25000 * 0.81}',
        }

        result = src_p.substitute(data)
        product_list.append(result)

    filename = f'{name}.pdf'
    file = open(filename, "w+b")

    data = {

        # Invoice data
        'consecutivo': 'CR1',
        # 'CUFE': signing.dumps(str('hola'), key='3U8A#XFG,,u@Z)', compress=True),

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
    pisaStatus = pisa.CreatePDF(result, dest=file)
    file.close()
    return pisaStatus.err
