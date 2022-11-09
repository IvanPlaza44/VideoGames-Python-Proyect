from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class CreacionDeusuario(UserCreationForm):
    username= forms.CharField(label= 'Usuario' ,max_length=20)
    password1=forms.CharField(label='Contraseña:',  widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir Contraseña:',widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={key:'' for key in fields}