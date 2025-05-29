from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name= "index"),
    path("novedades/", novedades),
    path("acerca_de/", acerca_de)
]