"""
Accounts app utilities
"""

# Django Tenants
from django_tenants.utils import schema_context

# Accounts models
from apps.accounts.models import User

# Django
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def create_superuser(schema_name):
    """
    create_superuser create the admin in new tenant
    """
    with schema_context(schema_name):
        User.objects.create_user(username='admin', password='admin')


def get_app_data(schema_name):
    command = 'tenant_command dumpdata'
    manage = os.path.join(settings.BASE_DIR, 'manage.py')

    output = open(f'{schema_name}.json', 'w')
    os.system(f'{manage} {command} --schema={schema_name} --indent=4 > {schema_name}.json')
    output.close()

    fs = FileSystemStorage("")
    with fs.open(f'{schema_name}.json') as json:
        response = HttpResponse(json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="'+schema_name+'"'
        os.remove(f'{schema_name}.json')
        return response
