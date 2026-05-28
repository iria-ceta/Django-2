"""
Lógica de control de la aplicación (Vistas).
Consulta los datos al ORM y renderiza las plantillas HTML correspondientes.
"""

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Author, Post, Tag


def starting_page(request):
    # Obtiene los 3 posts más recientes ordenados por fecha de publicación
    posts = Post.objects.all().order_by('-data_publicacio')[:3]
    return render(request, "blog/index.html", {
        "posts": posts
    })


def posts(request):
    # Obtiene el listado completo de todos los posts
    posts = Post.objects.all()
    return render(request, "blog/posts.html", {
        "posts": posts
    })


def post_detail(request, slug):
    # Obtiene un post por su slug o devuelve un error 404 si no existe
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {
        "post": post
    })


def author_list(request):
    # Obtiene el listado completo de todos los autores
    authors = Author.objects.all()
    return render(request, "blog/authors.html", {"authors": authors})


def author_detail(request, id):
    # Obtiene un autor por su ID o devuelve un error 404 si no existe
    author = get_object_or_404(Author, id=id)
    return render(request, "blog/author_detail.html", {
        "author": author
    })


def tag_list(request):
    # Obtiene el listado completo de todas las etiquetas (tags)
    tags = Tag.objects.all()
    return render(request, "blog/tags.html", {"tags": tags})


def tag_detail(request, id):
    # Obtiene una etiqueta por su ID o devuelve un error 404 si no existe
    tag = get_object_or_404(Tag, id=id)
    return render(request, "blog/tag_detail.html", {
        "tag": tag
    })