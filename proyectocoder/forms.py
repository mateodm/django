from django import forms
from proyectocoder.models import *

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
