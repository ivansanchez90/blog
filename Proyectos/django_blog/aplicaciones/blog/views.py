from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def generales(request):
    return render(request, "categorias/generales.html")