from rest_framework import serializers
from .models import Entregas

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Entregas
        fields=('__all__')
