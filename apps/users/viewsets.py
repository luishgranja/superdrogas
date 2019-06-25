"""
Users viewsets

Viewsets and views of the users app
"""

# Django Rest Framework
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import action

# Users models
from .models import UserModel

# Users serializers
from .serializers import (
    UserSerializer,
    LoginSerializer,
    ChangePasswordSerializer
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

    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        login is used to define a user's login action
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        user = UserSerializer(user).data
        data = {
            'user': {
                'id': user.get('id'),
                'username': user.get('username'),
                'name': user.get('name'),
            },
            'token': token
        }
        return Response(data)


class ChangePasswordView(UpdateAPIView):
    """
    Change password view

    View to change a user's password
    """
    model = UserModel
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        """
        update is used to update a user's password
        """
        user = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # check old password
            if not user.check_password(serializer.data.get('old_password')):
                return Response(
                    {'old_password': ['Wrong password.']},
                    status=status.HTTP_400_BAD_REQUEST
                )
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response(
                {'message': 'Changed sucessfully.'},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
