from django import forms

class VideojuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    desarrollador = forms.CharField(max_length=20)
    genero = forms.CharField(max_length=30)
    plataformas = forms.CharField(max_length=40)    
    jugadores = forms.IntegerField()
    lanzamiento = forms.CharField(max_length=40)
    resumen = forms.CharField(max_length=40)

class BusquedaVideojuegos(forms.Form):
    nombre=forms.CharField(max_length=30)