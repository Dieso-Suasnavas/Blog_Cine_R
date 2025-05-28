from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("Pagina inicio")

def novedades(request):
    return HttpResponse("Pagina de novedades")

def acerca_de(request):
    return HttpResponse("Pagina de acerca de")