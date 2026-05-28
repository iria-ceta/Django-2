"""
Configuración interna de la aplicación del Blog.
Registra el módulo y define sus propiedades base dentro del ecosistema de Django.
"""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Define los metadatos y la configuración base para la app 'blog'.
    """
    # Nombre único con el que Django identificará esta aplicación del proyecto
    name = 'blog'