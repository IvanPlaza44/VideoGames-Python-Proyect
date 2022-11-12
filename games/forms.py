from django import forms
class VideojuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    desarrollador = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    plataformas = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    jugadores = forms.IntegerField()
    lanzamiento = forms.DateField()
    distribuidor = forms.CharField(max_length=30)
    caratula = forms.ImageField(required=False) 
    autor= forms.CharField(max_length=30)
    fecha_de_creacion=forms.DateField()
    
class BusquedaVideojuego(forms.Form):
    nombre=forms.CharField(max_length=30, required=False)
