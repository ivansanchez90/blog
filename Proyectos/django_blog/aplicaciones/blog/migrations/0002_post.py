# Generated by Django 4.0 on 2021-12-16 17:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Título')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('descripcion', models.CharField(max_length=110, verbose_name='Descripción')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.URLField(max_length=255)),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]