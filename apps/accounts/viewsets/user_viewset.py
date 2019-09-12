"""
User viewset

Viewset to user serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Accounts models
from apps.accounts.models import User

# Accounts serializers
from apps.accounts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset

    CRUD views of the user serializer
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()
