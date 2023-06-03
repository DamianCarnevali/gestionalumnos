from django.urls import path, include
from rest_framework import routers
from .views import DatosEstudiantesViewSet, EstudiantesViewSet, EstudiantesCompletosViewSet

routers = routers.DefaultRouter()
routers.register(r'estudiantes', EstudiantesViewSet)
routers.register(r'datosestudiantes', DatosEstudiantesViewSet)
routers.register(r'estudiantescompletos', EstudiantesCompletosViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
