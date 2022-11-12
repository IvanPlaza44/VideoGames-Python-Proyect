from django import forms
class VideojuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    desarrollador = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    plataformas = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    jugadores = forms.IntegerField()
    lanzamiento = forms.DateField()
    resumen = forms.CharField(max_length=30)
    autor= forms.CharField(max_length=30)
    fecha_de_creacion=forms.DateField()
    