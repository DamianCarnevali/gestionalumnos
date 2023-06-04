from django.urls import path, include
from rest_framework import routers
from .views import ProfesoresViewSet, DetallesProfesoresViewSet, ProfesoresCompletosViewSet, ProfesoresMateriasViewSet

routers = routers.DefaultRouter()
routers.register(r'profesores', ProfesoresViewSet)
routers.register(r'detallesprofesores', DetallesProfesoresViewSet)
routers.register(r'profesores/completos', ProfesoresCompletosViewSet)
routers.register(r'relacion/profesores/materias', ProfesoresMateriasViewSet)

urlpatterns = [
    path('', include(routers.urls))
]