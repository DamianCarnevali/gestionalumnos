from rest_framework import viewsets, permissions
from gestiondealumnos.swagger import CustomAutoSchema
from drf_yasg.utils import swagger_auto_schema
from .models import Materias, Carreras
from .serializers import MateriasSerializer, CarrerasSerializer


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class MateriasViewSet(viewsets.ModelViewSet):
    queryset = Materias.objects.all()
    serializer_class = MateriasSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        correlativas_data = self.request.data.get('correlativas', [])
        materias = serializer.save()
        for correlativa_nombre in correlativas_data:
            correlativa = Materias.objects.get(nombre=correlativa_nombre)
            materias.correlativas.add(correlativa)

    def perform_update(self, serializer):
        correlativas_data = self.request.data.get('correlativas', [])
        materias = serializer.save()
        materias.correlativas.clear()
        for correlativa_nombre in correlativas_data:
            correlativa = Materias.objects.get(nombre=correlativa_nombre)
            materias.correlativas.add(correlativa)


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class CarrerasViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    serializer_class = CarrerasSerializer
    permission_classes = [permissions.IsAuthenticated]
