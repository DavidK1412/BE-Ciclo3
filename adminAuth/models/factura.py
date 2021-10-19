from django.db import models
from .venta import Venta

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField('Cliente', max_length=256, default='_')
    venta = models.ForeignKey(Venta, related_name='fact', on_delete=models.CASCADE)   