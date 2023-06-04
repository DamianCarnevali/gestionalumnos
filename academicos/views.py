from rest_framework import viewsets, permissions
from gestiondealumnos.swagger import CustomAutoSchema
from drf_yasg.utils import swagger_auto_schema
from .models import AcademicosEstudiantes, InscripcionesCursadas, InscripcionesFinales
from .serializers import AcademicosEstudiantesSerializer, InscripcionesCursadasSerializer, InscripcionesFinalesSerializer


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class AcademicosEstudiantesViewSet(viewsets.ModelViewSet):
    queryset = AcademicosEstudiantes.objects.all()
    serializer_class = AcademicosEstudiantesSerializer
    permission_classes = [permissions.IsAuthenticated]


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class InscripcionesCursadasViewSet(viewsets.ModelViewSet):
    queryset = InscripcionesCursadas.objects.all()
    serializer_class = InscripcionesCursadasSerializer
    permission_classes = [permissions.IsAuthenticated]


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class InscripcionesFinalesViewSet(viewsets.ModelViewSet):
    queryset = InscripcionesFinales.objects.all()
    serializer_class = InscripcionesFinalesSerializer
    permission_classes = [permissions.IsAuthenticated]
