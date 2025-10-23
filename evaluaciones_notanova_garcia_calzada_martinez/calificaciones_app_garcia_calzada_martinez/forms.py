from django import forms
from .models import Calificacion


class CalificacionForm(forms.ModelForm):
    """
    Formulario para crear y editar calificaciones.
    Excluye el campo 'promedio' ya que se calcula automáticamente.
    """
    
    class Meta:
        model = Calificacion
        fields = ['nombre_estudiante', 'identificacion', 'asignatura', 'nota1', 'nota2', 'nota3']
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ingrese el nombre completo'
            }),
            'identificacion': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej: 1234567890'
            }),
            'asignatura': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej: Matemáticas'
            }),
            'nota1': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00 - 100.00',
                'step': '0.01',
                'min': '0',
                'max': '100'
            }),
            'nota2': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00 - 100.00',
                'step': '0.01',
                'min': '0',
                'max': '100'
            }),
            'nota3': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00 - 100.00',
                'step': '0.01',
                'min': '0',
                'max': '100'
            }),
        }
        labels = {
            'nombre_estudiante': 'Nombre del Estudiante',
            'identificacion': 'Identificación',
            'asignatura': 'Asignatura',
            'nota1': 'Primera Nota',
            'nota2': 'Segunda Nota',
            'nota3': 'Tercera Nota',
        }

    def clean(self):
        """Validación adicional de notas"""
        cleaned_data = super().clean()
        nota1 = cleaned_data.get('nota1')
        nota2 = cleaned_data.get('nota2')
        nota3 = cleaned_data.get('nota3')

        # Validar que todas las notas estén en el rango válido
        for nota, nombre in [(nota1, 'nota1'), (nota2, 'nota2'), (nota3, 'nota3')]:
            if nota is not None and (nota < 0 or nota > 100):
                self.add_error(nombre, 'La nota debe estar entre 0 y 100.')

        return cleaned_data
