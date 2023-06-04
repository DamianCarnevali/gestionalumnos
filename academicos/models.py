from django.db import models
from estudiantes.models import Estudiantes
from carreras.models import Materias


class AcademicosEstudiantes(models.Model):
    nota_cierre1 = models.IntegerField(verbose_name='Primer nota')
    nota_cierre2 = models.IntegerField(verbose_name='Segunda nota')
    porcentaje_asistencia = models.IntegerField(verbose_name='Porcentaje de asistencia')
    resultado_cursada = models.BooleanField(verbose_name='Cursada aprobada')
    final = models.IntegerField(verbose_name='Nota final')
    fecha_final = models.DateField(verbose_name='Fecha del final')
    tomo = models.CharField(max_length=255, verbose_name='Tomo')
    folio = models.CharField(max_length=255, verbose_name='Folio')
    estudiantes = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    materias = models.ForeignKey(Materias, on_delete=models.CASCADE)


class InscripcionesCursadas(models.Model):
    fecha_inscripcion = models.DateField(verbose_name='Fecha de inscripción')
    curso = models.CharField(max_length=255, verbose_name='Curso')
    division = models.CharField(max_length=255, verbose_name='División')
    tipo_inscripcion = models.BooleanField(verbose_name='Regular o Libre')
    estudiantes = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    materias = models.ForeignKey(Materias, on_delete=models.CASCADE)


class InscripcionesFinales(models.Model):
    fecha_inscripcion = models.DateField(verbose_name='Fecha de inscripción al final')
    estudiantes = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    materias = models.ForeignKey(Materias, on_delete=models.CASCADE)