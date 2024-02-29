from django.urls import path, include
from Tanques.views import TanquesListView


urlpatterns = [
    path('', TanquesListView.as_view(), name='gestion_tanques')
]
