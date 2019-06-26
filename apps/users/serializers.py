"""
Users serializers

Serializers of the users app
"""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.exceptions import ValidationError

# Django Rest Framework
from rest_auth.serializers import PasswordResetSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Users models
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer

    For execute the CRUD actions in the user model
    """
    password = serializers.CharField()
    password_confirmation = serializers.CharField(source='password')

    class Meta:
        model = UserModel
        fields = (
            'id',
            'username',
            'name',
            'last_name',
            'email',
            'is_active',
            'password',
            'password_confirmation',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'password_confirmation': {'write_only': True}
        }

    def validate_password(self, value):
        """
        validate_password confirms if the password and the
        confirmation of the password match
        """
        data = self.get_initial()
        password_confirmation = data.get('password_confirmation')
        if value != password_confirmation:
            raise ValidationError("Passwords do not match.")
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)
