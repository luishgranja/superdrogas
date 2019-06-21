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
        """
        validate_password confirms if the password
        and the confirmation of the password match
        """
        data = self.get_initial()
        password_confirmation = data.get('password_confirmation')
        if value != password_confirmation:
            raise ValidationError("Passwords don't match.")
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 20)
    password = serializers.CharField(min_length = 8, max_length = 64)

    def validate_username(self, value):
        try:
            user = UserModel.objects.get(username = value)
        except UserModel.DoesNotExist:
            raise ValidationError('User does not exist.')
        if not user.is_active:
            raise ValidationError('User is not active.')
        self.context['user'] = user
        return value

    def validate(self, data):
        user = authenticate(
            username = data['username'],
            password = data['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid credentials.')
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user = self.context['user'])
        return self.context['user'], token.key