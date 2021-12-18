from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Post, Categoria
from django.shortcuts import get_object_or_404




def home(request):
    posts = Post.objects.filter(estado = True)
    context = {'posts':posts}
    return render(request, "index.html",context)

def detallePost(request,slug):
    post = get_object_or_404(Post,slug = slug)
    return render(request,'post.html',{'detalle_post':post})




def generales(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'General'))
    context = {'posts':posts}
    return render(request, "categorias/generales.html",context)

def accionclima(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Acción por el Clima'))
    context = {'posts':posts}
    return render(request, "categorias/accion_clima.html",context)

def agualimpia(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Agua Limpia y Saneamiento'))
    context = {'posts':posts}
    return render(request, "categorias/agua_limpia.html",context)

def alianzaobjetivos(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Alianzas Para Lograr Los Objetivos'))
    context = {'posts':posts}
    return render(request, "categorias/alianza_objetivos.html",context)

def ciudadessostenibles(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Ciudades y Comunidades Sostenibles'))
    context = {'posts':posts}
    return render(request, "categorias/ciudades_sostenibles.html",context)

def educacioncalidad(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Educación de Calidad'))
    context = {'posts':posts}
    return render(request, "categorias/educacion_calidad.html",context)

def energiasostenible(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Energía Sostenible y No Contaminable'))
    context = {'posts':posts}
    return render(request, "categorias/energia_sostenible.html",context)

def finpobreza(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Fin de la pobreza'))
    context = {'posts':posts}
    return render(request, "categorias/fin_pobreza.html",context)

def hambrecero(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Hambre Cero'))
    context = {'posts':posts}
    return render(request, "categorias/hambre_cero.html",context)

def igualdadgenero(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Igualdad de Género'))
    context = {'posts':posts}
    return render(request, "categorias/igualdad_genero.html",context)

def industria(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Industria, Innovación e Infraestructura'))
    context = {'posts':posts}
    return render(request, "categorias/industria.html",context)

def pazjusticia(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Paz, Justicia e Instituciones Sólidas'))
    context = {'posts':posts}
    return render(request, "categorias/paz_justicia.html",context)

def produccionconsumo(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Producción y Consumo Responsable'))
    context = {'posts':posts}
    return render(request, "categorias/produccion_consumo.html",context)

def reducciondesigualdad(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Reducción de las Desigualdades'))
    context = {'posts':posts}
    return render(request, "categorias/reduccion_desigualdad.html",context)

def saludbienestar(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Salud y Bienestar'))
    context = {'posts':posts}
    return render(request, "categorias/salud_bienestar.html",context)

def trabajodecente(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Trabajo Decente y Crecimiento Económico'))
    context = {'posts':posts}
    return render(request, "categorias/trabajo_decente.html",context)

def vidaecosistema(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Vida de Ecosistemas Terrestres'))
    context = {'posts':posts}
    return render(request, "categorias/vida_ecosistema.html",context)

def vidasubmarina(request):
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Vida Submarina'))
    context = {'posts':posts}
    return render(request, "categorias/vida_submarina.html",context)


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