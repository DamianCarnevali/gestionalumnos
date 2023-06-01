from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Estudiantes, DatosEstudiantes
from .serializers import EstudiantesSerializer, DatosEstudiantesSerializer


class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EstudiantesSerializer


class DatosEstudiantesViewSet(viewsets.ModelViewSet):
    queryset = DatosEstudiantes.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DatosEstudiantesSerializer
