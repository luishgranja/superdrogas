"""
Login view

Viewset to user serializer
"""

# Django Rest Framework
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

# Accounts serializer
from apps.accounts.serializers import (
    LoginSerializer,
    UserSerializer
)


class LoginView(CreateAPIView):
    """
    Login view

    Execute the logic to perform the user and client login
    """
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        """
        create get user's token
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        user = UserSerializer(user).data
        data = {
            'user': user,
            'token': token
        }
        return Response(data)
