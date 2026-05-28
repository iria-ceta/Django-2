from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Author, Tag

def starting_page(request):
    # Carga los últimos 3 posts ordenados por fecha de forma descendente
    posts = Post.objects.all().order_by('-data_publicacio')[:3]
    return render(request, "blog/index.html", {
        "posts": posts
    })

def posts(request):
    posts = Post.objects.all()
    return render(request, "blog/posts.html", {
        "posts": posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {
        "post": post
    })

def author_list(request):
    authors = Author.objects.all()
    return render(request, "blog/authors.html", {"authors": authors})

def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, "blog/author_detail.html", {
        "author": author
    })

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "blog/tags.html", {"tags": tags})

def tag_detail(request, id):
    tag = get_object_or_404(Tag, id=id)
    return render(request, "blog/tag_detail.html", {
        "tag": tag
    })