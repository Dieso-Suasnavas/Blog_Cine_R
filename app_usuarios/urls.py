from django.urls import path
from .views import *

urlpatterns = [
    path("perfil_formulario/", perfil_usuario, name= "formulario")
]
