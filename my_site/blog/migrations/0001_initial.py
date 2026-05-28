"""
Fichero de migración inicial generado automáticamente por Django.
Crea la estructura de tablas (Author, Tag y Post) en la base de datos.
"""

# Generado por Django 6.0.4 el 2026-05-27 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Define las operaciones secuenciales para inicializar la base de datos.
    """

    # Indica que es la primera migración de la app
    initial = True

    # Sin dependencias previas por ser el archivo inicial
    dependencies = [
    ]

    # Operaciones que se ejecutarán en la base de datos
    operations = [
        
        # Creación del modelo Author
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        
        # Creación del modelo Tag
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        
        # Creación del modelo Post y sus relaciones
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contingut', models.TextField()),
                ('imatge', models.ImageField(blank=True, null=True, upload_to='posts_images')),
                ('data_publicacio', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                
                # Relación 1-a-Muchos con Author (Si se borra el autor, el campo pasa a NULL)
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.author')),
                
                # Relación Muchos-a-Muchos con Tag (Crea una tabla intermedia)
                ('tags', models.ManyToManyField(related_name='posts', to='blog.tag')),
            ],
        ),
    ]