"""
Project utilities
"""

# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Django Tenants
from django_tenants.utils import schema_context

# Accounts models
from apps.accounts.models import User

# Pharmacies models
from apps.pharmacies.models import Pharmacy


def send_reset_password_email(user_pk):
    """
    send_reset_password_email send reset password email
    """
    user = User.objects.get(pk=user_pk)
    subject = f'Welcome @{user.username}!'
    content = render_to_string(
        'accounts/reset_password.html',
        {'user': user}
    )
    from_email = 'Super Drogas <superdrogas.contacto@gmail.com>'

    email = EmailMultiAlternatives(subject, content, from_email, [user.email])
    email.attach_alternative(content, "text/html")
    email.send()


def get_tenant_info(schema_name):
    """
    get_tenant_info return the first tenant object by schema_name
    """
    with schema_context(schema_name):
        return Pharmacy.objects.filter(schema_name=schema_name).first()
