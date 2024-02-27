#from django.http import HttpResponse
from django.shortcuts import render
from .models import Tanques
# Create your views here.

def home(request):
    tanquesList=Tanques.objects.all()
    return render(request, "tanques_view.html", {"tanques" : tanquesList})