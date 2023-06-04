from rest_framework import viewsets, permissions
from .models import AcademicosEstudiantes, InscripcionesCursadas, InscripcionesFinales
from .serializers import AcademicosEstudiantesSerializer, InscripcionesCursadasSerializer, InscripcionesFinalesSerializer


class AcademicosEstudiantesViewSet(viewsets.ModelViewSet):
    queryset = AcademicosEstudiantes.objects.all()
    serializer_class = AcademicosEstudiantesSerializer
    permission_classes = [permissions.IsAuthenticated]


class InscripcionesCursadasViewSet(viewsets.ModelViewSet):
    queryset = InscripcionesCursadas.objects.all()
    serializer_class = InscripcionesCursadasSerializer
    permission_classes = [permissions.IsAuthenticated]


class InscripcionesFinalesViewSet(viewsets.ModelViewSet):
    queryset = InscripcionesFinales.objects.all()
    serializer_class = InscripcionesFinalesSerializer
    permission_classes = [permissions.IsAuthenticated]
