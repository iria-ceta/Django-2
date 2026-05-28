from django.contrib import admin
from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    list_display = ("titulo", "data_publicacio", "author")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)