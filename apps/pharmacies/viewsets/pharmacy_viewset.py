"""
Pharmacy viewset

Viewset to pharmacy serializer
"""

# Django Rest Framework
from rest_framework import viewsets

# Pharmacies models
from apps.pharmacies.models import (
    Domain,
    Pharmacy
)

# Pharmacies serializers
from apps.pharmacies.serializers import PharmacySerializer


class PharmacyViewSet(viewsets.ModelViewSet):
    """
    Product viewset

    CRUD views of the product serializer
    """
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

    def perform_destroy(self, instance):
        """
        perform_destroy is used to performance a logic delete
        """
        instance.is_active = not instance.is_active
        instance.save()

    def perform_update(self, serializer):
        """
        perform_update is used to update domain model
        """
        pharmacy = serializer.save()
        domain = Domain.objects.get(tenant_id=pharmacy.id)
        domain.domain = f'{pharmacy.schema_name}.localhost'
        domain.save()
