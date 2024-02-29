from django.shortcuts import render, redirect
from .models import config
from django.views.generic import ListView

# Create your views here.
def home(request):
    configList=config.objects.all()

    data={
        'titulo'    : 'Configuración',
        'tanques'   : 'configList'
    }
    return render(request, "config_view.html", data)

class ConfigListView(ListView):
    model=config
    template_name='config_view.html'


def registrar_config(request):
    num_puntos=request.POST['txtnum_puntos']
    num_entregas=request.POST['txtnum_entregas']
    

    configuracion =config.objects.create(num_puntos=num_puntos, num_entregas=num_entregas)
    return redirect('/configuracion/')