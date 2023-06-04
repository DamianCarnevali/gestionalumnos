from django.db import models
from carreras.models import Materias

class DetallesProfesores(models.Model):
    sexo = models.CharField(max_length=255, verbose_name='Sexo')
    nacionalidad = models.CharField(max_length=255, verbose_name='Nacionalidad')
    titulo_base = models.CharField(max_length=255, verbose_name='Título de base')
    ano_egreso = models.IntegerField(verbose_name='Año de egreso')
    tramo_pedagogico = models.BooleanField(verbose_name='Posee tramo pedagógico')
    domicilio = models.CharField(max_length=255, verbose_name='Domicilio')
    numero = models.CharField(max_length=255, verbose_name='Número')
    codigo_postal = models.CharField(max_length=255, verbose_name='Código postal')
    localidad = models.CharField(max_length=255, verbose_name='Localidad')
    partido = models.CharField(max_length=255, verbose_name='Partido')
    provincia = models.CharField(max_length=255, verbose_name='Provincia')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')


class Profesores(models.Model):
    dni = models.CharField(max_length=255, unique=True, verbose_name='DNI')
    apellido = models.CharField(max_length=255, verbose_name='Apellido')
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    celular = models.CharField(max_length=255, verbose_name='Celular')
    correo = models.CharField(max_length=255, verbose_name='Correo particular')
    correo_abc=models.CharField(max_length=255, verbose_name='Correo ABC')
    detalles_profesores = models.ForeignKey(DetallesProfesores, on_delete=models.CASCADE)
    
    
class ProfesoresMaterias(models.Model):
    profesores = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    materias = models.ForeignKey(Materias, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['profesores', 'materias'], name='unique_profesores_materias'),
        ]