from django import forms

class UsuarioFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    correo_electronico=forms.CharField(max_length=30)
    fecha_de_nacimiento=forms.DateField(required=False)
    sexo=forms.CharField(max_length=15)
    

class BusquedaUsuario(forms.Form):
    nombre=forms.CharField(max_length=30)
    