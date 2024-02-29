from django.shortcuts import render
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