from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "app_pagina/inicio.html")

def novedades(request):
    return HttpResponse("Pagina de novedades")

def acerca_de(request):
    return HttpResponse("Pagina de acerca de")