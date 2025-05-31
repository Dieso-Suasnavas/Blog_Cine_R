from django.shortcuts import render
from .forms import PerfilForm

# Create your views here.

def perfil_usuario(request):
    form = PerfilForm()
    return render(request, "app_usuarios/inicio_perfil.html", {"form": form})