"""
User test
"""

# Django
from django.test import TestCase

# Accounts models
from apps.accounts.models import User


class UserTestCase(TestCase):
    """
    User test

    Validate the CRUD user actions
    """
    def setUp(self):
        User.objects.create(
            username='ivanmtoroc',
            identification_number='1010059777',
            first_name='Iván',
            last_name='Toro',
            email='ivanmtoroc@gmail.com',
            phone='3182539232',
            address='Cr. 3 # 8B'
        )

    def test_user_username(self):
        """
        All users save their username correctly
        """
        user = User.objects.get(identification_number='1010059777')
        self.assertEqual(user.username, 'ivanmtoroc')
