from django.urls import path, include
from rest_framework import routers
from .views import DatosEstudiantesViewSet, EstudiantesViewSet, EstudiantesCompletosViewSet, EstudiantesMateriasViewSet

routers = routers.DefaultRouter()
routers.register(r'', EstudiantesViewSet)
routers.register(r'', DatosEstudiantesViewSet)
routers.register(r'', EstudiantesCompletosViewSet)
routers.register(r'', EstudiantesMateriasViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
