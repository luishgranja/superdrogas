# Django Rest Framework
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import action


# Users models
from .models import UserModel
# Users serializers
from .serializers import UserSerializer, ChangePasswordSerializer, LoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset

    Define all views to user model
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = not user.is_active
        user.save()
        data = {'message': 'Changed sucessfully.'}
        return Response(data)

    @action(detail=False, methods=['post'])
    def login(self, request, pk=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        user = UserSerializer(user).data
        data = {
            'user': {
                'id': user.get('id'),
                'identification': user.get('identification'),
                'username': user.get('username'),
                'email': user.get('email'),
                'name': '{} {}'.format(user.get('first_name'), user.get('last_name')),
                'position': user.get('position')
            },
            'token': token
        }
        return Response(data)


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    @classmethod
    def get_extra_actions(cls):
        return []

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

