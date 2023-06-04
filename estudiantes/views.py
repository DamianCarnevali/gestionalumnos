from rest_framework import viewsets, permissions
from .models import Estudiantes, DatosEstudiantes, EstudiantesMaterias
from .serializers import EstudiantesSerializer, DatosEstudiantesSerializer, EstudiantesCompletosSerializer, EstudiantesMateriasSerializers


class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EstudiantesSerializer


class DatosEstudiantesViewSet(viewsets.ModelViewSet):
    queryset = DatosEstudiantes.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DatosEstudiantesSerializer


class EstudiantesCompletosViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EstudiantesCompletosSerializer


class EstudiantesMateriasViewSet(viewsets.ModelViewSet):
    queryset = EstudiantesMaterias.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EstudiantesMateriasSerializers
