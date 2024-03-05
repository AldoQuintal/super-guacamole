from django.urls import path, include
from Tanques.views import TanquesListView, eliminar_tanque, register, registrar_tanque, edit_tanque,delete_punto, editar_tanque, editar_config, edit_config, registrar_config ,eliminar_config ,configuracion, tabla_cubicaje, registro_puntos,ConfigListView
from api.views import consulta_entrega
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('tanques/', TanquesListView.as_view(), name='gestion_tanques'),
    path('registrarTanque/', registrar_tanque),
    path('tanques/eliminacionTanques/<int:id>', eliminar_tanque ),
    path('tanques/edicionTanques/<int:id>', edit_tanque ),
    path('editarTanque/', editar_tanque ),
    path('configuracion/', configuracion ),
    path('registrarConfig/', registrar_config), 
    path('eliminacionConfig/<int:id>', eliminar_config ),
    path('editarConfig/', editar_config ),
    path('edicionConfig/', edit_config ),
    path('consulta_entrega/', consulta_entrega),
    path('tanques/tablaCubicaje/<int:id_rex>', tabla_cubicaje),
    path('registroTablaCubicaje/', registro_puntos),
    path('tanques/tablaCubicaje/eliminacionPuntos/<int:id_rex>', delete_punto),
    path('register/', register),
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'), 
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),


    
    #path('configuracion/', ConfigListView.as_view(), name='gestion_configuracion')
    
]


