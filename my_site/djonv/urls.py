"""
Configuración de rutas globales del proyecto 'djonv'.
Se encarga de delegar el enrutamiento principal hacia el panel de administración
y de incluir las rutas específicas de la aplicación 'blog' mediante include().
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Panel de administración global de Django
    path('admin/', admin.site.urls),
    
    # Redirige cualquier ruta raíz o subruta directamente al archivo urls.py de la app 'blog'
    path("", include("blog.urls")),
]