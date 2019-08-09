"""
Pharmacy serializer

Serializer to pharmacy model
"""

# Django Rest Framework
from rest_framework import serializers

# Pharmacies models
from apps.pharmacies.models import (
    Domain,
    Pharmacy
)


class PharmacySerializer(serializers.ModelSerializer):
    """
    Pharmacy serializer

    Execute CRUD actions in the pharmacy model
    """
    class Meta:
        model = Pharmacy
        fields = '__all__'

    def create(self, validated_data):
        pharmacy = Pharmacy(
            schema_name=validated_data['schema_name'],
            name=validated_data['name']
        )
        pharmacy.save()
        domain = Domain(
            domain=f"{validated_data['schema_name']}.localhost",
            tenant_id=pharmacy.id,
        )
        domain.save()
        return pharmacy
