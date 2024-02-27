from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Entregas

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Entregas.objects.all()
    serializer_class = ProgrammerSerializer
