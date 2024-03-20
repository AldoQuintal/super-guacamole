from django.db import models

# Create your models here.

class Entregas(models.Model):
    vr_tanque = models.CharField(max_length=20)
    fecha_ini = models.CharField(max_length=20)
    fecha_fin = models.CharField(max_length=20)
    vol_ini = models.CharField(max_length=20)
    vol_fin = models.CharField(max_length=20)
    vol_ct_ini = models.CharField(max_length=20)
    vol_ct_fin = models.CharField(max_length=20)
    agua_ini = models.CharField(max_length=10)
    agua_fin = models.CharField(max_length=10)
    temp_ini = models.CharField(max_length=10)
    temp_fin = models.CharField(max_length=10)
    aum_neto = models.CharField(max_length=20)
    aum_bruto = models.CharField(max_length=20)
    clv_prd = models.CharField(max_length=10)

class inventarios(models.Model):
    vr_tanque = models.CharField(max_length=10)
    vr_fecha = models.CharField(max_length=30)
    vr_volumen = models.CharField(max_length=20)
    vr_vol_ct = models.CharField(max_length=20)
    vr_agua = models.CharField(max_length=20)
    vr_temp = models.CharField(max_length=20)
    vol_ant = models.CharField(max_length=20)

    class Meta:
        db_table = 'inventarios'


