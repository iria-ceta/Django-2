"""
Configuración del panel de administración de Django.
Registra los modelos y personaliza la interfaz visual para gestionar los datos.
"""

from django.contrib import admin
# Importa los tres modelos definidos en tu aplicación
from .models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    """
    Personalización de la interfaz de administración para el modelo Post.
    """
    # Rellena el slug automáticamente en tiempo real al escribir el título en el admin
    prepopulated_fields = {"slug": ("titulo",)}
    
    # Columnas que se mostrarán ordenadas en la lista general de posts dentro del admin
    list_display = ("titulo", "data_publicacio", "author")


# Registra el modelo Post aplicando la configuración personalizada de PostAdmin
admin.site.register(Post, PostAdmin)

# Registra el modelo Author con la interfaz estándar por defecto
admin.site.register(Author)

# Registra el modelo Tag con la interfaz estándar por defecto
admin.site.register(Tag)