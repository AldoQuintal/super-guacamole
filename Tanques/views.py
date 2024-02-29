#from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tanques
# Create your views here.

def home(request):
    tanquesList=Tanques.objects.all()

    data={
        'titulo'    : 'Regitro de Tanques',
        'tanques'   : 'tanquesList'
    }
    return render(request, "tanques_view.html", data)

class TanquesListView(ListView):
    model=Tanques
    template_name='tanques_view.html'

    def get_queryset(self):       
        return Tanques.objects.all()

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de Tanques'
        return context
    
def registrar_tanque(request):
    num_tanque=request.POST['txtnum_tanque']
    producto=request.POST['txtprodcuto']
    description=request.POST['txtdescripcion']
    capacidad=request.POST['txtcapacidad']
    altura=request.POST['txtaltura']

    tanque =Tanques.objects.create(num_tanque=num_tanque, producto=producto, descripcion=description, capacidad=capacidad, altura=altura)
    return redirect('/')

def eliminar_tanque(request, id):
    tanque=Tanques.objects.get(id=id)
    tanque.delete()

    return redirect('/')


