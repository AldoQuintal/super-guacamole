from rest_framework import serializers
from .models import inventarios

class InventariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= inventarios
        fields=('__all__')
