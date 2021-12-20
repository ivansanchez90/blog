from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic.list import ListView
from .forms import PostForm, UserRegisterForm
from .models import Autor, Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q 
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView


def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, "index.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/generales.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/accion_clima.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/agua_limpia.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/alianza_objetivos.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/ciudades_sostenibles.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/educacion_calidad.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/energia_sostenible.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/fin_pobreza.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/hambre_cero.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/igualdad_genero.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/industria.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/paz_justicia.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/produccion_consumo.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/reduccion_desigualdad.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/salud_bienestar.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/trabajo_decente.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/vida_ecosistema.html",{'posts':posts})

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
        paginator = Paginator(posts,2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    
    return render(request, "categorias/vida_submarina.html",{'posts':posts})

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

class PostCreateView(CreateView):
    model = Post
class PostUpdateView(UpdateView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post

def post(request):
    current_user = get_object_or_404(Autor, pk=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'usuarios/create.html', {'form':form})