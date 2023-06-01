from django.db import models


class DatosEstudiantes(models.Model):
    id = models.IntegerField(primary_key=True)
    sexo = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=255)
    secundario = models.CharField(max_length=255)
    ano_egreso_secundario = models.IntegerField()
    domicilio = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    partido = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()


class Estudiantes(models.Model):
    id = models.IntegerField(primary_key=True)
    dni = models.CharField(max_length=255, unique=True)
    apellido = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    datos_estudiantes = models.ForeignKey(
        DatosEstudiantes, on_delete=models.CASCADE)
