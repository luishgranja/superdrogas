"""
Users viewsets

Viewsets and views of the users app
"""

# Django Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response

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

    def destroy(self, request, *args, **kwargs):
        """
        destroy is used to performance a logic delete
        """
        user = self.get_object()
        user.is_active = not user.is_active
        user.save()
        data = {'message': 'Updated sucessfully.'}
        return Response(data)
