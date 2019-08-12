"""
Sales model

Model to manage commerce
"""

# Django
from django.db import models

# Accounts models
from apps.accounts.models.user_model import User

class SaleInvoice(models.Model):
    """
    SaleInvoice model

    """
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    client_id = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
    sale_type = models.CharField(max_length=50)
    date = models.DateField()
    total_amount = models.IntegerField()
    #is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user_id.username} {self.date}'