#from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tanques, configuration
# Create your views here.

def home(request):
    tanquesList=Tanques.objects.all()

    data={
        'titulo'    : 'Regitro de Tanques',
        'tanques'   : tanquesList
    }
    return render(request, "tanques_view.html", data)

class TanquesListView(ListView):
    model=Tanques
    template_name='tanques_view.html'

    def get_queryset(self):       
        return Tanques.objects.all()

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        print(f'Context : {context.get('object_list')}')
        context['titulo'] = 'Registro de Tanques'
        return context
    

def registrar_tanque(request):
    

    print("Registando Tanque ###")
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


def edit_tanque(request, id):
    tanque=Tanques.objects.get(id=id)
    data={
        'titulo'    : 'Edición de tanque',
        'tanque'   : tanque
    }

    return render(request, "edicionTanque.html", data)


def editar_tanque(request):
    id = int(request.POST['id'])
    num_tanque=request.POST['txtnum_tanque']
    producto=request.POST['txtprodcuto']
    description=request.POST['txtdescripcion']
    capacidad=request.POST['txtcapacidad']
    altura=request.POST['txtaltura']

    tanque=Tanques.objects.get(id=id)
    tanque.num_tanque = num_tanque
    tanque.producto = producto
    tanque.descripcion = description
    tanque.capacidad = capacidad
    tanque.altura = altura
    tanque.save()

    #tanque =Tanques.objects.create(num_tanque=num_tanque, producto=producto, descripcion=description, capacidad=capacidad, altura=altura)
    return redirect('/')

# Create your views here.
def configuracion(request):
    configList=configuration.objects.all()

    data={
        'titulo'    : 'Configuración',
        'config'   : configList
    }
    return render(request, "config_view.html", data)

class ConfigListView(ListView):
    model=configuration
    template_name='config_view.html'

def registrar_config(request):
    num_puntos=request.POST['txtnum_puntos']
    num_entregas=request.POST['txtnum_entregas']

    tanque =configuration.objects.create(num_puntos=num_puntos, num_entregas=num_entregas)
    return redirect('/configuracion/')

def eliminar_config(request, id):
    conf=configuration.objects.get(id=id)
    conf.delete()

    return redirect('/configuracion/')

def edit_config(request, id):
    conf=configuration.objects.get(id=id)
    data={
        'titulo'    : 'Edición de configuración',
        'conf'   : conf
    }

    return render(request, "edicionConfig.html", data)

def editar_config(request):
    id = int(request.POST['id'])
    num_puntos=request.POST['txtnum_puntos']
    num_entregas=request.POST['txtnum_entregas']
    

    conf=configuration.objects.get(id=id)
    conf.num_puntos = num_puntos
    conf.num_entregas = num_entregas
    conf.save()

    #tanque =Tanques.objects.create(num_tanque=num_tanque, producto=producto, descripcion=description, capacidad=capacidad, altura=altura)
    return redirect('/configuracion/')

