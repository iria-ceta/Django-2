from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.starting_page, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail-page'),
    path('authors', views.author_list, name='author-list-page'),
    path('authors/<int:id>', views.author_detail, name='author-detail-page'),
    path('tags', views.tag_list, name='tag-list-page'),
    path('tags/<int:id>', views.tag_detail, name='tag-detail-page'),
]