"""
Users viewsets

Viewsets and views of the users app
"""

# Django Rest Framework
from rest_framework import viewsets

# Users models
from .models import UserModel

# Users serializers
from .serializers import (
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset

    To define the CRUD views of the user model and login action
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()
