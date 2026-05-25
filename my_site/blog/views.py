from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

def starting_page(request):
    # Carga los últimos 3 posts ordenados por fecha de forma descendente
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })

def author_list(request):
    authors = Author.objects.all()
    return render(request, "blog/authors.html", {"authors": authors})

def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, "blog/author_detail.html", {
        "author": author,
        "posts": author.posts.all()
    })

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "blog/tags.html", {"tags": tags})

def tag_detail(request, id):
    tag = get_object_or_404(Tag, id=id)
    return render(request, "blog/tag_detail.html", {
        "tag": tag,
        "posts": tag.posts.all()
    })