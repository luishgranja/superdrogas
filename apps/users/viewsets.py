# Django Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Users models
from .models import UserModel

# Users serializers
from .serializers import UserSerializer


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
        data = {'message': 'Deleted successfully.'}
        return Response(data)
