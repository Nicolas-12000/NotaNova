from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Calificacion
from .forms import CalificacionForm

def crear_calificacion(request):
	"""Vista para crear una nueva calificación"""
	if request.method == 'POST':
		form = CalificacionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('calificaciones:listar_calificaciones')
	else:
		form = CalificacionForm()
    
	return render(request, 'calificaciones/crear.html', {'form': form})


def listar_calificaciones(request):
	"""Vista para listar todas las calificaciones y mostrar el promedio general"""
	calificaciones = Calificacion.objects.all()
	promedio_general = Calificacion.objects.aggregate(Avg('promedio'))['promedio__avg']
    
	# Si no hay registros, promedio_general será None
	if promedio_general is not None:
		promedio_general = round(promedio_general, 2)
    
	context = {
		'calificaciones': calificaciones,
		'promedio_general': promedio_general,
		'total_registros': calificaciones.count()
	}
    
	return render(request, 'calificaciones/listar.html', context)


def editar_calificacion(request, pk):
	"""Vista para editar una calificación existente"""
	calificacion = get_object_or_404(Calificacion, pk=pk)
    
	if request.method == 'POST':
		form = CalificacionForm(request.POST, instance=calificacion)
		if form.is_valid():
			form.save()
			return redirect('calificaciones:listar_calificaciones')
	else:
		form = CalificacionForm(instance=calificacion)
    
	context = {
		'form': form,
		'calificacion': calificacion
	}
    
	return render(request, 'calificaciones/editar.html', context)


def eliminar_calificacion(request, pk):
	"""Vista para eliminar una calificación"""
	calificacion = get_object_or_404(Calificacion, pk=pk)
    
	if request.method == 'POST':
		calificacion.delete()
		return redirect('calificaciones:listar_calificaciones')
    
	return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})


def promedio_general(request):
	"""Vista dedicada para mostrar el promedio general de todos los estudiantes"""
	promedio = Calificacion.objects.aggregate(Avg('promedio'))['promedio__avg']
	total_estudiantes = Calificacion.objects.values('identificacion').distinct().count()
	total_registros = Calificacion.objects.count()
    
	# Calcular promedio por estudiante
	estudiantes_promedio = Calificacion.objects.values(
		'nombre_estudiante', 'identificacion'
	).annotate(
		promedio_estudiante=Avg('promedio')
	).order_by('-promedio_estudiante')
    
	context = {
		'promedio_general': round(promedio, 2) if promedio else None,
		'total_estudiantes': total_estudiantes,
		'total_registros': total_registros,
		'estudiantes_promedio': estudiantes_promedio
	}
    
	return render(request, 'calificaciones/promedio_general.html', context)
