from django.db import models

# Create your models here.
class Tanques(models.Model):

    num_tanque = models.CharField(max_length=10)
    producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=20)
    altura = models.CharField(max_length=20)
    vr_tanque = models.CharField(max_length=20)
    inicia_entrega = models.CharField(max_length=20, default=False)
    vol_ref = models.CharField(max_length=20)
    fecha_ref = models.CharField(max_length=20)
    vol_ct_ref = models.CharField(max_length=20)