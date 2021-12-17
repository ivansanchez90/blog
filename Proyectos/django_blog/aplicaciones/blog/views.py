from django.shortcuts import render

def get_queryset(self):
    return self.objects.filter(estado=True)


def home(request):
    return render(request, "index.html")

def generales(request):
    return render(request, "categorias/generales.html")

def accionclima(request):
    return render(request, "categorias/accion_clima.html")

def agualimpia(request):
    return render(request, "categorias/agua_limpia.html")

def alianzaobjetivos(request):
    return render(request, "categorias/alianza_objetivos.html")

def ciudadessostenibles(request):
    return render(request, "categorias/ciudades_sostenibles.html")

def educacioncalidad(request):
    return render(request, "categorias/educacion_calidad.html")

def energiasostenible(request):
    return render(request, "categorias/energia_sostenible.html")

def finpobreza(request):
    return render(request, "categorias/fin_pobreza.html")

def hambrecero(request):
    return render(request, "categorias/hambre_cero.html")

def igualdadgenero(request):
    return render(request, "categorias/igualdad_genero.html")

def industria(request):
    return render(request, "categorias/industria.html")

def pazjusticia(request):
    return render(request, "categorias/paz_justicia.html")

def produccionconsumo(request):
    return render(request, "categorias/produccion_consumo.html")

def reducciondesigualdad(request):
    return render(request, "categorias/reduccion_desigualdad.html")

def saludbienestar(request):
    return render(request, "categorias/salud_bienestar.html")

def trabajodecente(request):
    return render(request, "categorias/trabajo_decente.html")

def vidaecosistema(request):
    return render(request, "categorias/vida_ecosistema.html")

def vidasubmarina(request):
    return render(request, "categorias/vida_submarina.html")