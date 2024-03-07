from django.urls import path, include
from django.urls import path, include 
from rest_framework import routers
from api import views
from Tanques.views import TanquesListView

router=routers.DefaultRouter()
router.register(r'entregas', views.ProgrammerViewSet)
router.register(r'inventarios', views.InventariosViewSet)


urlpatterns = [
    path('', include(router.urls)), 
    path('', TanquesListView.as_view(), name='gestion_tanques')
]
