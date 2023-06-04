from django.urls import path, include
from rest_framework import routers
from .views import AcademicosEstudiantesViewSet, InscripcionesCursadasViewSet, InscripcionesFinalesViewSet

routers = routers.DefaultRouter()
routers.register(r'', AcademicosEstudiantesViewSet)
routers.register(r'', InscripcionesCursadasViewSet)
routers.register(r'', InscripcionesFinalesViewSet)

urlpatterns = [
    path('', include(routers.urls))
]