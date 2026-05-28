"""
Configuración WSGI para el proyecto 'djonv'.
Expone el punto de entrada síncrono estándar para servidores web en producción.
"""

import os
from django.core.wsgi import get_wsgi_application

# Establece el archivo de configuración por defecto (settings.py) para el entorno de ejecución
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djonv.settings')

# Inicializa y expone la aplicación WSGI invocable por el servidor web
application = get_wsgi_application()