from django.urls import path, include
from Tanques.views import TanquesListView, eliminar_tanque, registrar_tanque


urlpatterns = [
    path('', TanquesListView.as_view(), name='gestion_tanques'),
    path('registrarTanque/', registrar_tanque),
    path('eliminacionTanques/<int:id>', eliminar_tanque )
]
