from django import forms
from .constantes import GENEROS

class PerfilForm(forms.Form):
    nombre_usuario = forms.CharField(max_length= 12, min_length= 6, help_text= "Ingresar nombre de usario", label= "Nombre de usuario")
    nombre = forms.CharField(max_length= 20, min_length= 3, help_text= "Ingresar nombre", label= "Nombre/s")
    apellido = forms.CharField(max_length= 15, min_length= 3, help_text= "Ingresar apellido", label= "Apallido")
    genero = forms.ChoiceField(choices= GENEROS, help_text= "Seleccionar genero", label= "Genero", required= False)
    fecha_de_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), help_text= "Seleccionar fecha de nacimiento", label= "Fecha de nacimiento")
    email = forms.EmailField(max_length= 30, help_text= "Ingresar correo electrónico", label= "Correo electrónico")
    password = forms.CharField(widget= forms.PasswordInput, max_length= 16, min_length= 6, help_text= "Ingresar contraseña", label= "Contraseña")