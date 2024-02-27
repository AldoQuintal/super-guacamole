from django.db import models

# Create your models here.
class Tanques(models.Model):

    num_tanque = models.CharField(max_length=10, string="Número de Tanque")
    producto = models.CharField(max_length=50, string="Producto")
    descripcion = models.CharField(max_length=50, string="Clave Producto")
    capacidad = models.CharField(max_length=20, string="Capacidad Total")
    altura = models.CharField(max_length=20, string="Altura del tanque")
    vr_tanque = models.CharField(max_length=20, invisible="1")
    inicia_entrega = models.CharField(max_length=20, default=False, invisible="1")
    vol_ref = models.CharField(max_length=20, invisible="1")
    fecha_ref = models.CharField(max_length=20, invisible="1")
    vol_ct_ref = models.CharField(max_length=20, invisible="1")