"""
Project utilities
"""

# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Accounts models
from apps.accounts.models import User


def send_reset_password_email(user_pk):
    """
    Send reset password email
    """
    user = User.objects.get(pk=user_pk)
    subject = f'Welcome @{user.username}!'
    content = render_to_string(
        'accounts/reset_password.html',
        {'user': user}
    )
    from_email = 'Super Drogas <noreply@superdrogas.co>'

    email = EmailMultiAlternatives(subject, content, from_email, [user.email])
    email.attach_alternative(content, "text/html")
    email.send()
