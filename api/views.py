from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Entregas
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
