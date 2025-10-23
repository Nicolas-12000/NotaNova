from django.contrib import admin

from .models import Calificacion


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
	"""Configuración del modelo Calificacion en el admin de Django"""
    
	list_display = ('nombre_estudiante', 'identificacion', 'asignatura', 'nota1', 'nota2', 'nota3', 'promedio')
	list_filter = ('asignatura',)
	search_fields = ('nombre_estudiante', 'identificacion', 'asignatura')
	ordering = ('-promedio', 'nombre_estudiante')
    
	fieldsets = (
		('Información del Estudiante', {
			'fields': ('nombre_estudiante', 'identificacion', 'asignatura')
		}),
		('Calificaciones', {
			'fields': ('nota1', 'nota2', 'nota3'),
			'description': 'El promedio se calculará automáticamente al guardar.'
		}),
	)
    
	readonly_fields = ('promedio',)
