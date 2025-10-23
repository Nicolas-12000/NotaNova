from django.db import models


class Calificacion(models.Model):
	"""
	Modelo para almacenar las calificaciones de estudiantes.
	Calcula automáticamente el promedio de las tres notas.
	"""
	nombre_estudiante = models.CharField(max_length=150, verbose_name="Nombre del Estudiante")
	identificacion = models.CharField(max_length=15, verbose_name="Identificación")
	asignatura = models.CharField(max_length=100, verbose_name="Asignatura")
	nota1 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Nota 1")
	nota2 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Nota 2")
	nota3 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Nota 3")
	promedio = models.DecimalField(max_digits=5, decimal_places=2, editable=False, verbose_name="Promedio")

	class Meta:
		verbose_name = "Calificación"
		verbose_name_plural = "Calificaciones"
		ordering = ['-promedio', 'nombre_estudiante']

	def calcular_promedio(self):
		"""Calcula el promedio de las tres notas"""
		return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)

	def save(self, *args, **kwargs):
		"""Guarda el registro calculando automáticamente el promedio"""
		self.promedio = self.calcular_promedio()
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.nombre_estudiante} - {self.asignatura} (Promedio: {self.promedio})"
