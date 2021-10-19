from django.db import models

class Venta(models.Model):
    id = models.BigAutoField(primary_key=True)
    fechaVenta = models.DateTimeField(auto_now_add=True)
    valor = models.IntegerField(default=0)
    descuento = models.IntegerField(default=0)
    productList = models.CharField('idProductos', max_length=256)
    valorTotal = models.IntegerField(default=0)