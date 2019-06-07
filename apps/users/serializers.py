# Django
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
# Django Rest Framework
from rest_framework import serializers

# Users models
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer

    To serialize http request and response:
    JSON to Python and vice versa
    """
    password = serializers.CharField()
    password_confirmation = serializers.CharField(source='password')

    class Meta:
        model = UserModel
        fields = (
            'id',
            'username',
            'name',
            'password',
            'password_confirmation'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'password_confirmation': {'write_only': True}
        }

    def validate_password(self, value):
        data = self.get_initial()
        password_confirmation = data.get('password_confirmation')
        if value != password_confirmation:
            raise ValidationError("Passwords don't match.")
        password_validation.validate_password(value)
        return value

    def create(self, data):
        return UserModel.objects.create_user(**data)
