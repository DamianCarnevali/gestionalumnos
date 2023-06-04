from django.db import models
from carreras.models import Materias


class DatosEstudiantes(models.Model):
    sexo = models.CharField(max_length=255, verbose_name='Sexo')
    nacionalidad = models.CharField(
        max_length=255, verbose_name='Nacionalidad')
    secundario = models.CharField(
        max_length=255, verbose_name='Título otorgado por el nivel secundario')
    ano_egreso_secundario = models.IntegerField(
        verbose_name='Año de egreso del nivel secundario')
    domicilio = models.CharField(max_length=255, verbose_name='Domicilio')
    numero = models.CharField(max_length=255, verbose_name='Número')
    codigo_postal = models.CharField(
        max_length=255, verbose_name='Código Postal')
    localidad = models.CharField(max_length=255, verbose_name='Localidad')
    partido = models.CharField(max_length=255, verbose_name='Partido')
    provincia = models.CharField(max_length=255, verbose_name='Provincia')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')

    class Meta:
        verbose_name = 'Dato del estudiante'
        verbose_name_plural = 'Datos de los estudiantes'


class Estudiantes(models.Model):
    dni = models.CharField(max_length=255, unique=True, verbose_name='DNI')
    apellido = models.CharField(max_length=255, verbose_name='Apellido')
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    celular = models.CharField(
        max_length=255, verbose_name='Teléfono celular')
    correo = models.CharField(
        max_length=255, verbose_name='Correo electrónico')
    datos_estudiantes = models.ForeignKey(
        DatosEstudiantes, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['-dni']

    def __str__(self):
        return self.apellido

class EstudiantesMaterias(models.Model):
    estudiantes = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    materias = models.ForeignKey(Materias, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['estudiantes', 'materias'], name='unique_estudiantes_materias'),
        ]
