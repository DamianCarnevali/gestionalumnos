from django.urls import path, include
from rest_framework import routers
from .views import DatosEstudiantesViewSet, EstudiantesViewSet

routers = routers.DefaultRouter()
routers.register(r'estudiantes', EstudiantesViewSet)
routers.register(r'datosestudiantes', DatosEstudiantesViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
