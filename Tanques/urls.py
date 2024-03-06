from django.urls import path, include
from Tanques.views import home, eliminar_tanque, consulta_inventarios, signout, signin,register, registrar_tanque, edit_tanque,delete_punto, editar_tanque, editar_config, edit_config, registrar_config ,eliminar_config ,configuracion, tabla_cubicaje, registro_puntos,ConfigListView
from api.views import consulta_entrega
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('tanques/', home),
    path('registrarTanque/', registrar_tanque),
    path('tanques/eliminacionTanques/<int:id>', eliminar_tanque ),
    path('tanques/edicionTanques/<int:id>', edit_tanque ),
    path('editarTanque/', editar_tanque ),
    path('configuracion/', configuracion ),
    path('registrarConfig/', registrar_config), 
    path('eliminacionConfig/<int:id>', eliminar_config ),
    path('editarConfig/', editar_config ),
    path('configuracion/edicionConfig/<int:id>', edit_config ),
    path('consulta_entrega/', consulta_entrega),
    path('tanques/tablaCubicaje/<int:id_rex>', tabla_cubicaje),
    path('registroTablaCubicaje/', registro_puntos),
    path('tanques/tablaCubicaje/eliminacionPuntos/<int:id_rex>', delete_punto),
    path('accounts/register/', register),
    path('accounts/login/', signin, name='login'), 
    path('accounts/logout/', signout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inventarios/', consulta_inventarios),


    
    #path('configuracion/', ConfigListView.as_view(), name='gestion_configuracion')
    
]


