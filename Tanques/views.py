#from django.http import HttpResponse
from django.shortcuts import render
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