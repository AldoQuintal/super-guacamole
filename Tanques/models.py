from django.db import models

# Create your models here.
class Tanques(models.Model):

    num_tanque = models.SmallIntegerField(verbose_name="Número de Tanque")
    producto = models.CharField(max_length=50, verbose_name="Producto")
    descripcion = models.CharField(max_length=50, verbose_name="Clave Producto")
    capacidad = models.CharField(max_length=20, verbose_name="Capacidad Total")
    altura = models.CharField(max_length=20, verbose_name="Altura del tanque")
    vr_tanque = models.CharField(max_length=20, editable=False)
    inicia_entrega = models.CharField(max_length=20, default=False, editable=False)
    vol_ref = models.CharField(max_length=20, editable=False)
    fecha_ref = models.CharField(max_length=20, editable=False)
    vol_ct_ref = models.CharField(max_length=20, editable=False)


class monitoreoTanques(models.Model):
    vr_tanque = models.CharField(max_length=10)
    vr_fecha = models.CharField(max_length=20)
    vr_volumen = models.CharField(max_length=20)
    vr_vol_ct = models.CharField(max_length=20)
    vr_agua = models.CharField(max_length=20)
    vr_temp = models.CharField(max_length=20)

class configuration(models.Model):
    num_puntos = models.CharField(max_length=10, verbose_name="Número de puntos a Configurar")
    num_entregas = models.CharField(max_length=10, verbose_name="Número de entregas a guardar")

class tanqueT1(models.Model):
    nivel = models.SmallIntegerField()
    volumen = models.CharField()
    id_ref = models.CharField()
    class Meta:
        db_table = 't1'

class tanqueT2(models.Model):
    altura = models.CharField()
    volumen = models.CharField()
    id_ref = models.CharField()

    class Meta:
        db_table = 't2'

class tanqueT3(models.Model):
    altura = models.CharField()
    volumen = models.CharField()
    id_ref = models.CharField()
    class Meta:
        db_table = 't3'

class tanqueT4(models.Model):
    altura = models.CharField()
    volumen = models.CharField()
    id_ref = models.CharField()
    class Meta:
        db_table = 't4'