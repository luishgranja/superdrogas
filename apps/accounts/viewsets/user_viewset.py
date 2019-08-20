"""
User viewset

Viewset to user serializer
"""

# Django Rest Framework
from rest_framework import viewsets
from rest_framework.decorators import action

# Accounts models
from apps.accounts.models import User

# Accounts serializers
from apps.accounts.serializers import UserSerializer

# Utilities
from superdrogas.utilities import send_reset_password_email


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

    @action(detail=True, methods=['get'])
    def reset_password(self, request, pk=None):
        user = self.get_object()
        send_reset_password_email(user_pk=user.id)
