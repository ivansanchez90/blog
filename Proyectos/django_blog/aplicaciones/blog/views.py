from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q 



def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset)
        ).distinct()
    context = {'posts':posts}
    return render(request, "index.html",context)

def detallePost(request,slug):
    post = get_object_or_404(Post,slug = slug)
    return render(request,'post.html',{'detalle_post':post})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'General'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'General'),
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/generales.html",context)

def accionclima(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Acción por el Clima'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Acción por el Clima')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/accion_clima.html",context)

def agualimpia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Agua Limpia y Saneamiento'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Agua Limpia y Saneamiento')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/agua_limpia.html",context)

def alianzaobjetivos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Alianzas Para Lograr Los Objetivos'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Alianzas Para Lograr Los Objetivos')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/alianza_objetivos.html",context)

def ciudadessostenibles(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Ciudades y Comunidades Sostenibles'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Ciudades y Comunidades Sostenibles')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/ciudades_sostenibles.html",context)

def educacioncalidad(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Educación de Calidad'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Educación de Calidad')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/educacion_calidad.html",context)

def energiasostenible(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Energía Sostenible y No Contaminable'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Energía Sostenible y No Contaminable')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/energia_sostenible.html",context)

def finpobreza(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Fin de la pobreza'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Fin de la pobreza')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/fin_pobreza.html",context)

def hambrecero(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Hambre Cero'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Hambre Cero')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/hambre_cero.html",context)

def igualdadgenero(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Igualdad de Género'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Igualdad de Género')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/igualdad_genero.html",context)

def industria(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Industria, Innovación e Infraestructura'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Industria, Innovación e Infraestructura')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/industria.html",context)

def pazjusticia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Paz, Justicia e Instituciones Sólidas'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Paz, Justicia e Instituciones Sólidas')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/paz_justicia.html",context)

def produccionconsumo(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Producción y Consumo Responsable'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Producción y Consumo Responsable')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/produccion_consumo.html",context)

def reducciondesigualdad(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Reducción de las Desigualdades'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Reducción de las Desigualdades')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/reduccion_desigualdad.html",context)

def saludbienestar(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Salud y Bienestar'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Salud y Bienestar')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/salud_bienestar.html",context)

def trabajodecente(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Trabajo Decente y Crecimiento Económico'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Trabajo Decente y Crecimiento Económico')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/trabajo_decente.html",context)

def vidaecosistema(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Vida de Ecosistemas Terrestres'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Vida de Ecosistemas Terrestres')
        ).distinct()
    context = {'posts':posts}
    return render(request, "categorias/vida_ecosistema.html",context)

def vidasubmarina(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, 
    categoria = Categoria.objects.get(nombre__iexact = 'Vida Submarina'))
    
    if queryset:
        posts = Post.objects.filter(
            
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Vida Submarina'),
        ).distinct()
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