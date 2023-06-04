from django.urls import path, include
from rest_framework import routers
from .views import AcademicosEstudiantesViewSet, InscripcionesCursadasViewSet, InscripcionesFinalesViewSet

routers = routers.DefaultRouter()
routers.register(r'datosacademicos/', AcademicosEstudiantesViewSet)
routers.register(r'inscripcion/cursada/', InscripcionesCursadasViewSet)
routers.register(r'inscripcion/final/', InscripcionesFinalesViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
