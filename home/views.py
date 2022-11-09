from contextvars import Context
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.template import Context, Template, loader
from home.forms import UsuarioFormulario,BusquedaUsuario
from home.models import Usuario

def crear_usuario(request):
    print(request.method)
    print(request.POST)
    if request.method=='POST':
        print("Estoy dentro del primer if ")
        formulario=UsuarioFormulario(request.POST)
        if formulario.is_valid():
            print("Estoy dentro del if")
            datos_crudos=formulario.cleaned_data
            nombre=datos_crudos['nombre']
            apellido=datos_crudos['apellido']
            edad=datos_crudos['edad']
            correo_electronico=datos_crudos['correo_electronico']
            fecha_de_nacimiento=datos_crudos['fecha_de_nacimiento']
            sexo=datos_crudos['sexo']
            usuario=Usuario(nombre=nombre,apellido=apellido,correo_electronico=correo_electronico,edad=edad,fecha_de_nacimiento=fecha_de_nacimiento,sexo=sexo)
            usuario.save()
            
        return redirect('usuario_creado')
    
    formulario=UsuarioFormulario()
    return render(request,'home/crear_usuario.html',{'formulario':formulario})

def ver_usuarios(request):
    #que vamos a buscar
    nombre=request.GET.get('nombre',None)
    if nombre:
        usuario=Usuario.objects.filter(nombre__icontains=nombre)
    else:
        usuario=Usuario.objects.all()
        
    formulario=BusquedaUsuario()
    return render(request,'home/ver_usuarios.html',{'usuario':usuario,'formulario':formulario})

def usuario_creado(request):
    return render(request,'home/usuario_creado.html',{})

def acerca_de_nosotros(request):
    return render(request,'home/acerca_de_nosotros.html',{})

def index(request):
    return render(request, 'home/index.html')

