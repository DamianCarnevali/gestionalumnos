from rest_framework import viewsets, permissions
from gestiondealumnos.swagger import CustomAutoSchema
from drf_yasg.utils import swagger_auto_schema
from .models import Estudiantes, DatosEstudiantes, EstudiantesMaterias
from .serializers import EstudiantesSerializer, DatosEstudiantesSerializer, EstudiantesCompletosSerializer, EstudiantesMateriasSerializers


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EstudiantesSerializer


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class DatosEstudiantesViewSet(viewsets.ModelViewSet):
    queryset = DatosEstudiantes.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DatosEstudiantesSerializer


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class EstudiantesCompletosViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EstudiantesCompletosSerializer


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class EstudiantesMateriasViewSet(viewsets.ModelViewSet):
    queryset = EstudiantesMaterias.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EstudiantesMateriasSerializers
