from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(verbose_name= "Nombre de usuario", max_length= 12, blank= False)
    nombre = models.CharField(verbose_name= "Nombre", max_length= 15, blank= False)
    apellido = models.CharField(verbose_name= "Apellido", max_length= 15, blank= False)
    fecha_nacimiento = models.DateField(verbose_name= "Fecha de nacimiento", blank= False)

    def __str__(self):
        return self.user.username