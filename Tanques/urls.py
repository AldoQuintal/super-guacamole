from django.urls import path, include
from Tanques.views import TanquesListView, eliminar_tanque


urlpatterns = [
    path('', TanquesListView.as_view(), name='gestion_tanques'),
    path('eliminacionTanques/<int:id>', eliminar_tanque )
]
