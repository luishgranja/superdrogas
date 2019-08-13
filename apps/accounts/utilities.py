"""
Accounts app utilities
"""

# Django Tenants
from django_tenants.utils import schema_context

# Accounts models
from apps.accounts.models import User


def create_superuser(schema_name):
    """
    create_superuser create the admin in new tenant
    """
    with schema_context(schema_name):
        User.objects.create_user(username='admin', password='admin')
