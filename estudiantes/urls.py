from django.urls import path, include
from rest_framework import routers
from .views import DatosEstudiantesViewSet, EstudiantesViewSet, EstudiantesCompletosViewSet

routers = routers.DefaultRouter()
routers.register(r'', EstudiantesViewSet)
routers.register(r'', DatosEstudiantesViewSet)
routers.register(r'', EstudiantesCompletosViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
