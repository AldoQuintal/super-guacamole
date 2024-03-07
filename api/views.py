from rest_framework import viewsets
from .serializer import ProgrammerSerializer, InventariosSerializer
from .models import Entregas, inventarios
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Entregas.objects.all()
    serializer_class = ProgrammerSerializer

# Create your views here.
@login_required
def consulta_entrega(request):
    apiList=Entregas.objects.all()

    data={
        'titulo'    : 'Consulta Entregas',
        'entrega'   : apiList
    }
    return render(request, "entregas_view.html", data)


### Inventarios ###
class InventariosViewSet(viewsets.ModelViewSet):
    queryset = inventarios.objects.all()
    serializer_class = InventariosSerializer

# Create your views here.
@login_required
def consulta_inventarios(request):
    invent=inventarios.objects.all()

    data={
        'titulo'    : 'Inventarios',
        'config'   : invent
    }
    return render(request, "inventarios.html", data)
