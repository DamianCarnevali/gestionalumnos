from rest_framework import viewsets, permissions
from gestiondealumnos.swagger import CustomAutoSchema
from drf_yasg.utils import swagger_auto_schema
from .models import Profesores, DetallesProfesores, ProfesoresMaterias
from .serializers import ProfesoresSerializers, DetallesProfesoresSerializer, ProfesoresMateriasSerializers, ProfesoresCompletosSerializers


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class ProfesoresViewSet(viewsets.ModelViewSet):
    queryset = Profesores.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfesoresSerializers


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class DetallesProfesoresViewSet(viewsets.ModelViewSet):
    queryset = DetallesProfesores.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DetallesProfesoresSerializer


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class ProfesoresCompletosViewSet(viewsets.ModelViewSet):
    queryset = Profesores.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfesoresCompletosSerializers


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class ProfesoresMateriasViewSet(viewsets.ModelViewSet):
    queryset = ProfesoresMaterias.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfesoresMateriasSerializers
