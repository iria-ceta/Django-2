"""
Configuración ASGI para el proyecto 'djonv'.
Expone el punto de entrada asíncrono para servidores web compatibles.
"""

import os
from django.core.asgi import get_asgi_application

# Define el archivo de configuración (settings.py) por defecto del proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djonv.settings')

# Crea la aplicación ASGI ejecutable
application = get_asgi_application()