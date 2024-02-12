from django import forms
from proyectocoder.models import *
from django.contrib.auth.models import User

class RemeraForm(forms.ModelForm):
    class Meta:
        model = Remeras
        fields = ['nombre', 'precio', 'talle', 'color']

class CalzadoForm(forms.ModelForm):
    class Meta:
        model = Calzado
        fields = ['modelo', 'precio', 'talle', 'estado']

class GorraForm(forms.ModelForm):
    class Meta:
        model = Gorras
        fields = ['nombre', 'color', 'precio']

""" class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Vuelve a escribir la contraseña", widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields} """