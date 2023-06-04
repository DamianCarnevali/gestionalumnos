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

        # Limpiar correlativas que no corresponden
        for correlativa_actual in materias.correlativas.all():
            if correlativa_actual.nombre not in correlativas_data:
                materias.correlativas.remove(correlativa_actual)

    def perform_update(self, serializer):
        correlativas_data = self.request.data.get('correlativas', [])
        materias = serializer.save()

        # Limpiar correlativas existentes
        materias.correlativas.clear()

        # Agregar correlativas actualizadas
        for correlativa_nombre in correlativas_data:
            correlativa = Materias.objects.get(nombre=correlativa_nombre)
            materias.correlativas.add(correlativa)

        # Limpiar correlativas que no corresponden
        for correlativa_actual in materias.correlativas.all():
            if correlativa_actual.nombre not in correlativas_data:
                materias.correlativas.remove(correlativa_actual)


@swagger_auto_schema(auto_schema=CustomAutoSchema)
class CarrerasViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    serializer_class = CarrerasSerializer
    permission_classes = [permissions.IsAuthenticated]
