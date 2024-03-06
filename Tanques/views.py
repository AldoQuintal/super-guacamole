#from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tanques, configuration, tanqueT1, tanqueT2, tanqueT3, tanqueT4
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    tanquesList=Tanques.objects.all().order_by('num_tanque')

    data={
        'titulo'    : 'Regitro de Tanques',
        'tanques'   : tanquesList
    }
    return render(request, "tanques_view.html", data)

class TanquesListView(ListView):
    model=Tanques
    template_name='tanques_view.html'

    def get_queryset(self):       
        return Tanques.objects.all().order_by('num_tanque')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context
    

def registrar_tanque(request):

    num_tanque=request.POST['txtnum_tanque']
    print(f'Num_tanque: {num_tanque}')
    producto=request.POST['txtprodcuto']
    description=request.POST['txtdescripcion']
    capacidad=request.POST['txtcapacidad']
    altura=request.POST['txtaltura']

    tanque =Tanques.objects.create(num_tanque=num_tanque, producto=producto, descripcion=description, capacidad=capacidad, altura=altura)
    return redirect('/tanques/')

def eliminar_tanque(request, id):
    tanque=Tanques.objects.get(id=id)
    tank_id = tanque.num_tanque
    # Eliminamos todos los registros creados anteriormente 
    if tank_id == 1:
        tank_delete = tanqueT1.objects.all()
        tank_delete.delete()
    if tank_id == 2:
        tank_delete = tanqueT2.objects.all()
        tank_delete.delete()
    if tank_id == 3:
        tank_delete = tanqueT3.objects.all()
        tank_delete.delete()
    if tank_id == 4:
        tank_delete = tanqueT4.objects.all()
        tank_delete.delete()
    
    tanque.delete()
    
    return redirect('/tanques/')

@login_required
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
    return redirect('/tanques/')

# Create your views here.
@login_required
def configuracion(request):
    configList=configuration.objects.all()

    data={
        'titulo'    : 'Configuración',
        'config'   : configList
    }
    return render(request, "config_view.html", data)

@login_required
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

@login_required
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


# Create your views here.
@login_required
def tabla_cubicaje(request, id_rex):
    tanque_id=Tanques.objects.get(id=id_rex)
    tank_id = tanque_id.num_tanque
    print(f'tankid ------------- {tank_id}')
    if tank_id == 1:
        tanque=tanqueT1.objects.all().order_by('altura')
        print("Tank_id = 1 entrando al primer tanque ########")
        data={
            'titulo'    : 'Edición de tanque',
            'cubicaje'   : tanque, 
            'id'    : id_rex
        }

    if tank_id == 2:
        tanque=tanqueT2.objects.all().order_by('altura')
        print("Tank_id = 2 entrando al Segundo tanque ########")
        data={
            'titulo'    : 'Edición de tanque',
            'cubicaje'   : tanque, 
            'id'    : id_rex
        }

    if tank_id == 3:
        tanque=tanqueT3.objects.all().order_by('altura')
        print("Tank_id = 3 entrando al Tercer tanque ########")
        data={
            'titulo'    : 'Edición de tanque',
            'cubicaje'   : tanque, 
            'id'    : id_rex
        }

    if tank_id == 4:
        tanque=tanqueT4.objects.all().order_by('altura')
        print("Tank_id = 4 entrando al cuarto tanque ########")
        data={
            'titulo'    : 'Edición de tanque',
            'cubicaje'   : tanque, 
            'id'    : id_rex
        }

    return render(request, "tabla_cubicaje.html", data)

def registro_puntos(request):
    id = request.POST['id']
    print(f'Id en registro puntos: {id}')
    altura=request.POST['txtaltura']
    volumen=request.POST['txtvolumen']
    
    tanque=Tanques.objects.get(id=id)
    print(f'Tanques object: {tanque}')
    tank_id = tanque.num_tanque
    print(f'tank_id: {tank_id}')
    if tank_id == 1:
        tanque =tanqueT1.objects.create(altura=altura, volumen= volumen, id_ref=id)
    if tank_id == 2:
        tanque =tanqueT2.objects.create(altura=altura, volumen= volumen, id_ref=id)
    if tank_id == 3:
        tanque =tanqueT3.objects.create(altura=altura, volumen= volumen, id_ref=id)
    if tank_id == 4:
        tanque =tanqueT4.objects.create(altura=altura, volumen= volumen, id_ref=id)
        
    return redirect('/tablaCubicaje/{0}'.format(id))

def delete_punto(request, id_rex):
    tanque = Tanques.objects.all()
    for a in tanque:
        print(f'a.id : {a.id}')
        tablas = tanqueT1.objects.get(id=id_rex)
        print(f'tablas1: {tablas}')
        if tablas.id_ref:
            if int(tablas.id_ref) == int(a.id):
                print("Tanque 1 paso datos")
        
        tablas = tanqueT2.objects.get(id=id_rex)
        print(f'tablas2: {tablas}')
        if tablas.id_ref:
            if int(tablas.id_ref) == int(a.id):
                print("Tanque 2 paso datos")

    return redirect('/tanques/')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} ha sido creado')
            return redirect('/tanques/')
        
    else:
        form = UserRegisterForm()
        
    context = { 'form' : form }

    return render(request, 'register.html', context)