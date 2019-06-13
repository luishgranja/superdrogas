from rest_framework import serializers
from .models import Batch


class BatchSerialize(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('medicamento', 'cantidad', 'fecha_entrega', 'fecha_vencimiento')
