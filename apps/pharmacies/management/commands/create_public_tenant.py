"""
Create public tenant command
"""

# Django
from django.core.management.base import (
    BaseCommand,
    CommandError
)

# Pharmacies models
from apps.pharmacies.models import (
    Domain,
    Pharmacy
)


class Command(BaseCommand):
    """
    Create public tenant

    Command to create public tenant from the console
    """
    help = 'Create the public tenant registry for the project'

    def handle(self, *args, **options):
        public_tenant, created = Pharmacy.objects.get_or_create(
            schema_name='public',
            name='Public tenant'
        )

        if created:
            _, created = Domain.objects.get_or_create(
                domain='localhost',
                tenant_id=public_tenant.id
            )
            success_message = self.style.SUCCESS('Public tenant created successfully!')
            self.stdout.write(success_message)
        else:
            raise CommandError('Public tenant is already created')
