from django.db import models

# Create your models here.
class Tanques(models.Model):

    num_tanque = models.CharField(max_length=10, verbose_name="Número de Tanque")
    producto = models.CharField(max_length=50, verbose_name="Producto")
    descripcion = models.CharField(max_length=50, verbose_name="Clave Producto")
    capacidad = models.CharField(max_length=20, verbose_name="Capacidad Total")
    altura = models.CharField(max_length=20, verbose_name="Altura del tanque")
    vr_tanque = models.CharField(max_length=20, editable=False)
    inicia_entrega = models.CharField(max_length=20, default=False, editable=False)
    vol_ref = models.CharField(max_length=20, editable=False)
    fecha_ref = models.CharField(max_length=20, editable=False)
    vol_ct_ref = models.CharField(max_length=20, editable=False)