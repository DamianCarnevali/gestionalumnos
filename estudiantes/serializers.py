from rest_framework import serializers
from .models import Estudiantes, DatosEstudiantes


class DatosEstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosEstudiantes
        fields = ('id', 'sexo', 'nacionalidad', 'secundario', 'ano_egreso_secundario', 'domicilio',
                  'numero', 'codigo_postal', 'localidad', 'partido', 'provincia', 'fecha_nacimiento')


class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ('id', 'dni', 'apellido', 'nombre',
                  'celular', 'correo', 'datos_estudiantes')
