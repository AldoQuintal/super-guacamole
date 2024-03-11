#from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tanques, configuration, tanqueT1, tanqueT2, tanqueT3, tanqueT4
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
@login_required
def home(request):
    tanquesList=Tanques.objects.all().order_by('num_tanque')

    data={
        'titulo'    : 'Registro de Tanques',
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

    tanq_list = Tanques.objects.all()
    for i in tanq_list:
        print(f'i.numtanque: {i.num_tanque}, num_tanque: {num_tanque}')
        if int(i.num_tanque) == int(num_tanque):

            data={
            'titulo'    : 'Registro de Tanques',
            'tanques'   : tanq_list,
            'error' : 'El número de tanque ya ha sido registrado!'
            }
            return render(request, 'tanques_view.html', data)

    tanque =Tanques.objects.create(num_tanque=num_tanque, producto=producto, descripcion=description, capacidad=capacidad, altura=altura)
    return redirect('/tanques/')

def eliminar_tanque(request, id):
    tanque=Tanques.objects.get(id=id)
    tank_id = tanque.num_tanque
    # Eliminamos todos los registros creados anteriormente 
    if tank_id == 1:
        tank_delete = tanqueT1.objects.all().order_by('altura')
        tank_delete.delete()
    if tank_id == 2:
        tank_delete = tanqueT2.objects.all().order_by('altura')
        tank_delete.delete()
    if tank_id == 3:
        tank_delete = tanqueT3.objects.all().order_by('altura')
        tank_delete.delete()
    if tank_id == 4:
        tank_delete = tanqueT4.objects.all().order_by('altura')
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
    puerto = request.POST['txtcom_port']

    # Validación del puerto
    # /dev/tty
    print(f'Puerto : {puerto[0:8]}')
    if not ('/dev/tty') == puerto[0:8]:
        print("Son iguales Pasa")
        data={
        'titulo'    : 'Configuración',
        'error' : f'Sintaxis del puerto: {puerto}, no coincide con /dev/tty'
        }
        return render(request, "config_view.html", data)
    
    else:
        
        tanque =configuration.objects.create(num_puntos=num_puntos, num_entregas=num_entregas, puerto=puerto)
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

    print(f'Conf: {conf.puerto}')
    if not ('/dev/tty') == conf.puerto[0:8]:
        
        data={
        'titulo'    : 'Configuración',
        'error' : f'Sintaxis del puerto: {conf.puerto}, no coincide con /dev/tty'
        }
        return render(request, "edicionConfig.html", data)
    
    else:

        return render(request, "edicionConfig.html", data)

## Función para editar la configuración de los tanques ## 
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

## Crea el render de las respectivas tablas de cubicaje segun el tanque ##
# Create your views here.
@login_required
def tabla_cubicaje(request, id_rex):
    tanque_id=Tanques.objects.get(id=id_rex)
    tank_id = tanque_id.num_tanque
    print(f'tankid ------------- {tank_id}')
    if tank_id == 1:
        tanque=tanqueT1.objects.order_by('altura')
        print("Tank_id = 1 entrando al primer tanque ########")
        data={
            'titulo'    : 'Tablas T1',
            'cubicaje'   : tanque, 
            'id'    : id_rex
        }
        return render(request, "tabla_cubicaje_t1.html", data)

    if tank_id == 2:
        tanque=tanqueT2.objects.order_by('altura')
        print("Tank_id = 2 entrando al Segundo tanque ########")
        data={
            'titulo'    : 'Tablas T2',
            'cubicaje'   : tanque, 
            'id'    : id_rex
        }
        return render(request, "tabla_cubicaje_t2.html", data)

    if tank_id == 3:
        tanque=tanqueT3.objects.order_by('altura')
        print("Tank_id = 3 entrando al Tercer tanque ########")
        data={
            'titulo'    : 'Tablas T3',
            'cubicaje'   : tanque, 
            'id'    : id_rex
        }
        return render(request, "tabla_cubicaje_t3.html", data)

    if tank_id == 4:
        tanque=tanqueT4.objects.order_by('altura')
        print("Tank_id = 4 entrando al cuarto tanque ########")
        data={
            'titulo'    : 'Tablas T4',
            'cubicaje'   : tanque, 
            'id'    : id_rex
        }
        return render(request, "tabla_cubicaje_t4.html", data)
    
## Función para registrar puntos en la tabla de cubicaje ##
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
        punto = tanqueT1.objects.order_by('altura')
        for i in punto:
            if int(i.altura) == int(altura):
                data={
                'titulo'    : 'Tablas T1',
                'cubicaje'   : punto,
                'error' : 'El número de Altura ya ha sido registrado!',
                'id'    : i.id_ref, 
                }
                return render(request, 'tabla_cubicaje_t1.html', data)
            
        tanque =tanqueT1.objects.create(altura=altura, volumen= volumen, id_ref=id)
        return redirect('/tanques/tablaCubicajeT1/{0}'.format(id))
    
    if tank_id == 2:
        punto = tanqueT2.objects.order_by('altura')
        for i in punto:
            if int(i.altura) == int(altura):
                data={
                'titulo'    : 'Tablas T2',
                'cubicaje'   : punto,
                'error' : 'El número de Altura ya ha sido registrado!',
                'id'    : i.id_ref, 
                }
                return render(request, 'tabla_cubicaje_t2.html', data)
            
        tanque =tanqueT2.objects.create(altura=altura, volumen= volumen, id_ref=id)
        return redirect('/tanques/tablaCubicajeT2/{0}'.format(id))
    
    if tank_id == 3:
        punto = tanqueT3.objects.order_by('altura')
        for i in punto:
            if int(i.altura) == int(altura):
                data={
                'titulo'    : 'Tablas T3',
                'cubicaje'   : punto,
                'error' : 'El número de Altura ya ha sido registrado!',
                'id'    : i.id_ref, 
                }
                return render(request, 'tabla_cubicaje_t3.html', data)
            
        tanque =tanqueT3.objects.create(altura=altura, volumen= volumen, id_ref=id)
        return redirect('/tanques/tablaCubicajeT3/{0}'.format(id))
    
    if tank_id == 4:
        punto = tanqueT4.objects.order_by('altura')
        for i in punto:
            if int(i.altura) == int(altura):
                data={
                'titulo'    : 'Tablas T4',
                'cubicaje'   : punto,
                'error' : 'El número de Altura ya ha sido registrado!',
                'id'    : i.id_ref, 
                }
                return render(request, 'tabla_cubicaje_t4.html', data)
            
        tanque =tanqueT4.objects.create(altura=altura, volumen= volumen, id_ref=id)
        return redirect('/tanques/tablaCubicajeT4/{0}'.format(id))
        
    
## Función para borrar puntos de la tabla de cubicaje ##
def delete_punto_t1(request, id_rex):
    punto=tanqueT1.objects.get(id=id_rex)
    punto.delete()
    return redirect('/tanques/tablaCubicajeT1/{0}'.format(punto.id_ref))

def delete_punto_t2(request, id_rex):
    punto=tanqueT2.objects.get(id=id_rex)
    punto.delete()
    return redirect('/tanques/tablaCubicajeT2/{0}'.format(punto.id_ref))

def delete_punto_t3(request, id_rex):
    punto=tanqueT3.objects.get(id=id_rex)
    punto.delete()
    return redirect('/tanques/tablaCubicajeT3/{0}'.format(punto.id_ref))

def delete_punto_t4(request, id_rex):
    punto=tanqueT4.objects.get(id=id_rex)
    punto.delete()
    return redirect('/tanques/tablaCubicajeT4/{0}'.format(punto.id_ref))



###### Sistema de Registro, Login, Logout ######
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'form' : UserRegisterForm,
            'titulo': 'Register'
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                 #Registrando usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/tanques/')
            
            except:
                return render(request, 'register.html', {
                'form' : UserRegisterForm, 
                'error': 'Username already exists'
            })

        return render(request, 'register.html', {
                'form' : UserRegisterForm, 
                'error': 'Password do not match'
            })


def signout(request):
    logout(request)
    return redirect('login')

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
        'form' : AuthenticationForm,
        'titulo' : 'Login', 
        })  
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
            'form' : AuthenticationForm,
            'titulo' : 'Login', 
            'error': 'Username or Password is not correct'
            }) 
        else:
            login(request, user)
            return redirect('/tanques/')


