"""
Definició dels models de dades de l'aplicació.
Estructura les taules Author, Tag i Post utilitzant l'ORM de Django.
"""

from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    """
    Representa un autor del blog amb la seva informació de contacte.

    Attributes:
        name (str): Nom de l'autor.
        apellido (str): Cognom de l'autor.
        email (str): Correu electrònic de contacte.
    """
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        """
        Retorna el nom complet de l'autor per a la seva representació en text.
        """
        return f"{self.name} {self.apellido}"


class Tag(models.Model):
    """
    Representa una etiqueta o tag utilitzada per classificar els posts.

    Attributes:
        tag_name (str): Nom de l'etiqueta de classificació.
    """
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        """
        Retorna el nom de l'etiqueta per a la seva representació en text.
        """
        return self.tag_name


class Post(models.Model):
    """
    Representa una publicació o article individual dins del blog.

    Attributes:
        titulo (str): Títol de l'article.
        contingut (str): Text o cos principal de la publicació.
        imatge (File): Arxiu d'imatge adjunt a la publicació (opcional).
        data_publicacio (datetime): Data i hora de creació automàtica del post.
        author (Author): Relació de clau forana (1-a-Molts) amb el model Author.
        tags (ManyToManyField): Relació (Molts-a-Molts) amb el model Tag.
        slug (str): Text de la URL amigable generada per al SEO.
    """
    titulo = models.CharField(max_length=50)
    contingut = models.TextField()
    imatge = models.ImageField(upload_to='posts_images', null=True, blank=True)
    data_publicacio = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")    
    tags = models.ManyToManyField(Tag, related_name="posts")
    slug = models.SlugField(blank=True, null=False, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        """
        Genera el slug automàticament a partir del títol abans de desar el registre.
        
        Neteja el text convertint majúscules en minúscules i substituint espais per guions.
        """
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Retorna el títol de l'article per a la seva representació en text.
        """
        return self.titulo