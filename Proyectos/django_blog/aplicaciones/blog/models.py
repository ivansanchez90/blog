from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoría', max_length=100, null=False, blank=False)
    estado = models.BooleanField("Categoría Activada/Categoría no Activada", default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    nombres = models.CharField('Nombres de Autor', max_length=255, null=True, blank=True)
    apellidos = models.CharField('Apellidos de Autor', max_length=255, null=True, blank=True)
    estado = models.BooleanField('Autor Activo/No Activo', default = True)
    usuario_administrador = models.BooleanField(default=False)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
  
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)


    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título',max_length=90, blank=False, null=False)
    slug = models.CharField('Slug',max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripción',max_length=110, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
