from rest_framework import serializers
from .models import Profesores, DetallesProfesores, ProfesoresMaterias

class DetallesProfesoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesProfesores
        fields='__all__'
        
class ProfesoresMateriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfesoresMaterias
        fields='__all__'

class ProfesoresSerializers(serializers.ModelSerializer):
    materias=ProfesoresMateriasSerializers(many=True, read_only=True)
    class Meta:
        model = Profesores
        fields='__all__'
        
class ProfesoresCompletosSerializers(serializers.ModelSerializer):
    detallesprofesores=DetallesProfesoresSerializer(many=True, read_only=True)
    materias=ProfesoresMateriasSerializers(many=True, read_only=True)
    class Meta:
        model = Profesores
        fields='__all__'