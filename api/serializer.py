from rest_framework import serializers
from .models import Entregas, inventarios

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Entregas
        fields=('__all__')

class InventariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= inventarios
        fields=('__all__')
