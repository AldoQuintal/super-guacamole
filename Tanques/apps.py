from django.apps import AppConfig


class TanquesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Tanques'

class monitoreoTanquesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitoreoTanques'

class configurationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'configuration'
