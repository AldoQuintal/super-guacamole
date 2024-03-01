from django.urls import path, include
from config.views import ConfigListView, registrar_config


urlpatterns = [
    #path('', ConfigListView.as_view(), name='gestion_config'),
    path('registrarConfig/', registrar_config)
]
