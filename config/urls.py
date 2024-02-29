from django.urls import path, include
from config.views import ConfigListView


urlpatterns = [
    path('', ConfigListView.as_view(), name='gestion_config'),
    path('registrarTanque/', registrar_tanque),
]
