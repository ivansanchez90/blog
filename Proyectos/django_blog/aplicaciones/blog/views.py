from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Post, Categoria



def home(request):
    posts = Post.objects.filter(estado = True)
    context = {'posts':posts}
    return render(request, "index.html",context)

def generales(request):
    return render(request, "categorias/generales.html")

def accionclima(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Acción por el Clima'))
    return render(request, "categorias/accion_clima.html")

def agualimpia(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Agua Limpia y Saneamiento'))
    return render(request, "categorias/agua_limpia.html")

def alianzaobjetivos(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Alianzas Para Lograr Los Objetivos'))
    return render(request, "categorias/alianza_objetivos.html")

def ciudadessostenibles(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Ciudades y Comunidades Sostenibles'))
    return render(request, "categorias/ciudades_sostenibles.html")

def educacioncalidad(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Educación de Calidad'))
    return render(request, "categorias/educacion_calidad.html")

def energiasostenible(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Energía Sostenible y No Contaminable'))
    return render(request, "categorias/energia_sostenible.html")

def finpobreza(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Fin de la pobreza'))
    return render(request, "categorias/fin_pobreza.html")

def hambrecero(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Hambre Cero'))
    return render(request, "categorias/hambre_cero.html")

def igualdadgenero(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Igualdad de Género'))
    return render(request, "categorias/igualdad_genero.html")

def industria(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Industria, Innovación e Infraestructura'))
    return render(request, "categorias/industria.html")

def pazjusticia(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Paz, Justicia e Instituciones Sólidas'))
    return render(request, "categorias/paz_justicia.html")

def produccionconsumo(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Producción y Consumo Responsable'))
    return render(request, "categorias/produccion_consumo.html")

def reducciondesigualdad(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Reducción de las Desigualdades'))
    return render(request, "categorias/reduccion_desigualdad.html")

def saludbienestar(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Salud y Bienestar'))
    return render(request, "categorias/salud_bienestar.html")

def trabajodecente(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Trabajo Decente y Crecimiento Económico'))
    return render(request, "categorias/trabajo_decente.html")

def vidaecosistema(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Vida de Ecosistemas Terrestres'))
    return render(request, "categorias/vida_ecosistema.html")

def vidasubmarina(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre = 'Vida Submarina'))
    return render(request, "categorias/vida_submarina.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'usuarios/register.html',context)