from django.contrib import admin
from .models import Estudiantes, DatosEstudiantes


class EstudiantesInline(admin.TabularInline):
    model = Estudiantes
    max_num = 1


class DatosEstudiantesAdmin(admin.ModelAdmin):
    inlines = [EstudiantesInline]
    list_display = ('sexo', 'nacionalidad', 'secundario', 'ano_egreso_secundario', 'domicilio',
                    'numero', 'codigo_postal', 'localidad', 'partido', 'provincia', 'fecha_nacimiento')


admin.site.register(DatosEstudiantes, DatosEstudiantesAdmin)
