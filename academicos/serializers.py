from rest_framework import serializers
from .models import AcademicosEstudiantes, InscripcionesCursadas, InscripcionesFinales
from estudiantes.serializers import EstudiantesSerializer
from carreras.serializers import MateriasSerializer


class AcademicosEstudiantesSerializer(serializers.ModelSerializer):
    estudiantes = EstudiantesSerializer()
    materias = MateriasSerializer()

    class Meta:
        model = AcademicosEstudiantes
        fields = '__all__'


class InscripcionesCursadasSerializer(serializers.ModelSerializer):
    estudiantes = EstudiantesSerializer()
    materias = MateriasSerializer()

    class Meta:
        model = InscripcionesCursadas
        fields = '__all__'


class InscripcionesFinalesSerializer(serializers.ModelSerializer):
    estudiantes = EstudiantesSerializer()
    materias = MateriasSerializer()

    class Meta:
        model = InscripcionesFinales
        fields = '__all__'
