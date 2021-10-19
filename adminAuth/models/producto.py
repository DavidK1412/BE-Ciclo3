from django.db import models

class Producto(models.Model):
    id_Prod = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=50)
    LINKImg = models.CharField(max_length=256)
    Descripcion = models.CharField(max_length=256)
    ProdInven = models.IntegerField(default=0)
    Precio = models.IntegerField(default=0)