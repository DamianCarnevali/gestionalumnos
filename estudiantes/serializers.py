from rest_framework import serializers
from .models import Estudiantes, DatosEstudiantes, EstudiantesMaterias


class DatosEstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosEstudiantes
        fields = '__all__'

class EstudiantesMateriasSerializers(serializers.ModelSerializer):
    class Meta:
        model =EstudiantesMaterias
        fields='__all__'

class EstudiantesSerializer(serializers.ModelSerializer):
    materias=EstudiantesMateriasSerializers(many=True, read_only=True)
    class Meta:
        model = Estudiantes
        fields = '__all__'

class EstudiantesCompletosSerializer(serializers.ModelSerializer):
    datosestudiantes=DatosEstudiantesSerializer(many=True, read_only=True)
    materias=EstudiantesMateriasSerializers(many=True, read_only=True)
    class Meta:
        model=Estudiantes
        fields='__all__'