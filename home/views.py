from contextvars import Context
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.template import Context, Template, loader

from home.forms import UsuarioFormulario
from home.models import Usuario


def crear_usuario(request):
    if request.method=='POST':
        formulario=UsuarioFormulario(request.POST)
        if formulario.is_valid():
            datos_crudos=formulario.cleaned_data
            nombre=datos_crudos['nombre']
            apellido=datos_crudos['apellido']
            edad=datos_crudos['edad']
            correo_electronico=datos_crudos['correo_electronico']
            fecha_de_nacimiento=datos_crudos['fecha_de_nacimiento']
            sexo=datos_crudos['sexo']
            persona=Usuario(nombre=nombre,apellido=apellido,correo_electronico=correo_electronico,edad=edad,fecha_de_nacimiento=fecha_de_nacimiento,sexo=sexo)
            persona.save()
        return HttpResponse('El usuario se ha creado')
    
    formulario=UsuarioFormulario()
    return render(request,'home/crear_usuario.html',{'formulario':formulario})

def hola(request):
    return HttpResponse("<h1>Hola, Bienvenidos a nuestro Blog</h1>")

def index(request):
    return render(request, 'home/index.html')

