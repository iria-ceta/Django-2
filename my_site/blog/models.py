from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.apellido}"

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contingut = models.TextField()
    imatge = models.ImageField(upload_to='posts_images', null=True, blank=True)
    data_publicacio = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")    
    tags = models.ManyToManyField(Tag, related_name="posts")
    slug = models.SlugField(blank=True, null=False, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        """
        Genera el slug automàticament a partir del títol abans de desar.
        """
        if not self.slug:
            self.slug = slugify(self.titol)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo