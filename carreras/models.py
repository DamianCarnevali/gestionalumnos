from django.db import models

class Carreras(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    resolucion = models.CharField(max_length=255, verbose_name='Número de Resolución')
    titulacion = models.CharField(max_length=255, verbose_name='Título que otorga')
    duracion = models.CharField(max_length=255, verbose_name='Duración del Plan de Estudios')
    cantidad_materias = models.CharField(max_length=255, verbose_name='Cantidad de materias')
    
    class Meta:
        verbose_name='Carrera'
        verbose_name_plural='Carreras'


class Materias(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    carga_horaria_semanal = models.IntegerField(verbose_name='Horas semanales')
    carga_horaria_anual=models.IntegerField(verbose_name='Horas anuales')
    es_cuatrimestral=models.BooleanField()
    tipo_campo=models.CharField(max_length=255,verbose_name='Pertenece al campo de')
    cantidad_correlativa = models.IntegerField(verbose_name='Cantidad de materias correlativas')
    correlativas=models.ManyToManyField('self', blank=True, symmetrical=False)
    carreras = models.ForeignKey(Carreras, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Materia'
        verbose_name_plural='Materias'
        ordering=['-id']
        
    def __str__(self):
        return self.nombre
