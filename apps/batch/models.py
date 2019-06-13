from django.db import models


class Batch(models.Model):
    medicamento = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    fecha_entrega = models.DateField()
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.medicamento
