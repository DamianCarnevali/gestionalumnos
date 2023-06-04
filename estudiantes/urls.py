from django.urls import path, include
from rest_framework import routers
from .views import DatosEstudiantesViewSet, EstudiantesViewSet, EstudiantesCompletosViewSet, EstudiantesMateriasViewSet

routers = routers.DefaultRouter()
routers.register(r'estudiantes', EstudiantesViewSet)
routers.register(r'datosestudiantes', DatosEstudiantesViewSet)
routers.register(r'estudiantes/completos', EstudiantesCompletosViewSet)
routers.register(r'relacion/estudiantes/materias', EstudiantesMateriasViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
