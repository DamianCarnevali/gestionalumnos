from django.contrib import admin
from .models import AcademicosEstudiantes, InscripcionesCursadas, InscripcionesFinales

admin.site.register(AcademicosEstudiantes)
admin.site.register(InscripcionesCursadas)
admin.site.register(InscripcionesFinales)
