from django.urls import path, include
from Tanques.views import TanquesListView, eliminar_tanque, registrar_tanque, edit_tanque, editar_tanque, editar_config, edit_config, registrar_config ,eliminar_config ,configuracion, tabla_cubicaje,ConfigListView
from api.views import consulta_entrega


urlpatterns = [
    path('', TanquesListView.as_view(), name='gestion_tanques'),
    path('registrarTanque/', registrar_tanque),
    path('eliminacionTanques/<int:id>', eliminar_tanque ),
    path('edicionTanques/<int:id>', edit_tanque ),
    path('editarTanque/', editar_tanque ),
    path('configuracion/', configuracion ),
    path('registrarConfig/', registrar_config), 
    path('eliminacionConfig/<int:id>', eliminar_config ),
    path('editarConfig/', editar_config ),
    path('edicionConfig/<int:id>', edit_config ),
    path('consulta_entrega/', consulta_entrega),
    path('tablaCubicaje/<int:id>', tabla_cubicaje),
    
    #path('configuracion/', ConfigListView.as_view(), name='gestion_configuracion')
    
]


