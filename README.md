NotaNova - Mini proyecto Django

Estructura creada: app `calificaciones_app_garcia_calzada_martinez` con CRUD de Calificacion.

Pasos rápidos:

1. Activar el entorno virtual (Windows PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

2. Instalar dependencias (si tienes `requirements.txt`):

```powershell
pip install -r requirements.txt
```

3. Crear migraciones y migrar:

```powershell
python manage.py makemigrations
python manage.py migrate
```

4. Crear superusuario (opcional):

```powershell
python manage.py createsuperuser
```

5. Ejecutar servidor de desarrollo:

```powershell
python manage.py runserver
```

Notas:
- La app está registrada en `INSTALLED_APPS`.
- Templates en `templates/calificaciones/`.
- Static en `/static/`.
- Si tu entorno virtual tiene otro nombre actualiza `.gitignore`.
