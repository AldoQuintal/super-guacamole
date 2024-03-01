from django.urls import path, include
from Tanques.views import TanquesListView, eliminar_tanque, registrar_tanque, edit_tanque, editar_tanque
from config.views import ConfigListView, registrar_config, configuracion


urlpatterns = [
    path('', TanquesListView.as_view(), name='gestion_tanques'),
    path('registrarTanque/', registrar_tanque),
    path('eliminacionTanques/<int:id>', eliminar_tanque ),
    path('edicionTanques/<int:id>', edit_tanque ),
    path('editarTanque/', editar_tanque ),
    path('configuracion/', configuracion ),
    #path('registrarConfig/', registrar_config)
]


