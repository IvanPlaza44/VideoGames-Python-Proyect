from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from accounts.models import ExtesionUsuario
from accounts.forms import CreacionDeusuario
from django.contrib.auth.decorators import login_required
# Create your views here.

def iniciar_sesion(request):
    if request.method== 'POST':
        formulario= AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            usuario= formulario.get_user() #permite que se loege
            login(request,usuario)
            extensionUsuario,es_nuevo=ExtesionUsuario.objects.get_or_create(user=request.user)
            return redirect('index')
    else:
        formulario=AuthenticationForm()
    return render(request, 'accounts/iniciar_sesion.html',{'formulario':formulario})

def registrar(request):
    if request.method== 'POST':
        formulario=CreacionDeusuario(request.POST)
        if formulario.is_valid():
            #creacion de usuario
            formulario.save() #nos permite crear un usuario nuevo
            return redirect('index')
    else:
        formulario=CreacionDeusuario()        
    return render(request, 'accounts/registrar.html',{'formulario':formulario})

@login_required
def mi_perfil(request):
    return render(request, 'accounts/perfil_del_usuario.html',{})