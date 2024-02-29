from django.db import models

# Create your models here.
class config(models.Model):
    num_puntos = models.CharField(max_length=10, verbose_name="Número de puntos a Configurar")
    num_entregas = models.CharField(max_length=10, verbose_name="Número de entregas a guardar")

    