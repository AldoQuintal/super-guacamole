from django.shortcuts import render, redirect
from .models import config
from django.views.generic import ListView

# Create your views here.
def configuracion(request, id):
    configList=config.objects.get(id=id)

    data={
        'titulo'    : 'Configuración',
        'tanques'   : configList
    }
    return render(request, "config_view.html", data)

class ConfigListView(ListView):
    model=config
    template_name='config_view.html'


def registrar_config(request):
    id = int(request.POST['id'])
    num_puntos=request.POST['txtnum_puntos']
    num_entregas=request.POST['txtnum_entregas']
    global_config = config.objects.get(id=id)
    global_config.num_puntos = num_puntos
    global_config.num_entregas = num_entregas
    global_config.save()
    
    return redirect('/configuracion/')