from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AutorManager(BaseUserManager):
    def create_user(self,email,username,nombres, password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico!')

        usuario = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombres = nombres
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,username, email, nombres, password):
        usuario = self.create_user(
            email,
            username = username, 
            nombres = nombres,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario
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

class Autor(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    nombres = models.CharField('Nombres de Autor', max_length=255, null=True, blank=True)
    apellidos = models.CharField('Apellidos de Autor', max_length=255, null=True, blank=True)
    estado = models.BooleanField('Autor Activo/No Activo', default = True)
    usuario_administrador = models.BooleanField(default=False)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    objects = AutorManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres']
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
    
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
