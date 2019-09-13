"""
User serializer

Serializer to user model
"""

# Django
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

# Django Rest Framework
from rest_framework import serializers

# Accounts models
from apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer

    Execute CRUD actions in the user model
    """
    password = serializers.CharField()
    password_confirmation = serializers.CharField(source='password')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'identification_number',
            'rol',
            'rol_name',
            'email',
            'first_name',
            'last_name',
            'phone',
            'address',
            'is_active',
            'password',
            'password_confirmation',
        )

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
        """
        create save new user in database
        """
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        """
        to_representation define the data for the serializer response
        """
        data = super(UserSerializer, self).to_representation(instance)
        data.pop('password', None)
        data.pop('password_confirmation', None)
        return data
