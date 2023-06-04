from rest_framework import viewsets, permissions
from .models import Profesores, DetallesProfesores, ProfesoresMaterias
from .serializers import ProfesoresSerializers, DetallesProfesoresSerializer, ProfesoresMateriasSerializers, ProfesoresCompletosSerializers


class ProfesoresViewSet(viewsets.ModelViewSet):
    queryset = Profesores.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfesoresSerializers


class DetallesProfesoresViewSet(viewsets.ModelViewSet):
    queryset = DetallesProfesores.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DetallesProfesoresSerializer


class ProfesoresCompletosViewSet(viewsets.ModelViewSet):
    queryset = Profesores.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfesoresCompletosSerializers


class ProfesoresMateriasViewSet(viewsets.ModelViewSet):
    queryset = ProfesoresMaterias.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfesoresMateriasSerializers
