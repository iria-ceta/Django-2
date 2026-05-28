"""
Configuración del sistema de enrutamiento global del proyecto.
Mapea los patrones de URL hacia sus correspondientes funciones de vista en 'views'.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Rutas para posts: Inicio, Listado general y Detalle (por slug)
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.posts, name='posts-page'),
    path('posts/<slug:slug>/', views.post_detail, name='post-detail-page'),
    
    # Rutas para autores: Listado general y Detalle (por ID)
    path('authors/', views.author_list, name='author-list-page'),
    path('authors/<int:id>/', views.author_detail, name='author-detail-page'),
    
    # Rutas para etiquetas (tags): Listado general y Detalle (por ID)
    path('tags/', views.tag_list, name='tag-list-page'),
    path('tags/<int:id>/', views.tag_detail, name='tag-detail-page'),
]

# En modo desarrollo (DEBUG=True), sirve los archivos multimedia subidos por los usuarios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)