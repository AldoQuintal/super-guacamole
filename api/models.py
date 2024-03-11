from django.db import models

# Create your models here.

class Entregas(models.Model):
    vr_tanque = models.CharField(max_length=100)
    fecha_ini = models.CharField(max_length=100)
    fecha_fin = models.CharField(max_length=100)
    vr_volumen = models.CharField(max_length=100)
    vr_vol_ct = models.CharField(max_length=100)
    vr_agua = models.CharField(max_length=100)
    vr_temp = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class inventarios(models.Model):
    vr_tanque = models.CharField(max_length=10)
    vr_fecha = models.CharField(max_length=30)
    vr_volumen = models.CharField(max_length=20)
    vr_vol_ct = models.CharField(max_length=20)
    vr_agua = models.CharField(max_length=20)
    vr_temp = models.CharField(max_length=20)

    class Meta:
        db_table = 'inventarios'


