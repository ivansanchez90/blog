from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Post, Comment, Like, PostView, User

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'state', 'publish_date')
    resource_class = CategoriaResource

# class UserResource(resources.ModelResource):
#     class Meta:
#         model = User

# class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     search_fields = ['nombres', 'apellidos']
#     list_display = ('nombres', 'apellidos', 'estado', 'fecha_creacion')
#     resource_class = UserResource

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)
