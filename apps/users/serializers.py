"""
Users serializers

Serializers of the users app
"""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.exceptions import ValidationError

# Django Rest Framework
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
            'is_active',
            'password',
            'password_confirmation'
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


class ChangePasswordSerializer(serializers.Serializer):
    """
    Change password serializer

    For change the user's password
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class LoginSerializer(serializers.Serializer):
    """
    Login serializer

    For user login
    """
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate_username(self, value):
        """
        validate_username confirm if user exists
        """
        try:
            user = UserModel.objects.get(username=value)
        except UserModel.DoesNotExist:
            raise ValidationError('User does not exist.')

        if not user.is_active:
            raise ValidationError('User is not active.')

        self.context['user'] = user
        return value

    def validate(self, attrs):
        user = authenticate(
            username=attrs['username'],
            password=attrs['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid credentials.')
        return attrs

    def create(self, validated_data):
        token, _ = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
