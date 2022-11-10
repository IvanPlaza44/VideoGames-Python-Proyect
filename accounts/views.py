from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from accounts.models import ExtesionUsuario
from accounts.forms import CreacionDeusuario,EditarPerfilDeUsuario, CambioDeContraseña
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

# Create your views here.

def mi_login(request):
    if request.method== 'POST':
        formulario= AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            usuario= formulario.get_user() #permite que se loege
            login(request,usuario)
            extensionUsuario,es_nuevo=ExtesionUsuario.objects.get_or_create(user=request.user)
            return redirect('index')
    else:
        formulario=AuthenticationForm()
    return render(request, 'accounts/login.html',{'formulario':formulario})

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

@login_required
def editar_perfil(request):
    
    if request.method=='POST':
        formulario= EditarPerfilDeUsuario(request.POST, request.FILES)
        if formulario.is_valid():
            data_nueva=formulario.cleaned_data
            request.user.first_name=data_nueva['first_name']
            request.user.last_name=data_nueva['last_name']
            request.user.email=data_nueva['email']
            request.user.extesionusuario.avatar=data_nueva['avatar']
            request.user.extesionusuario.descripcion=data_nueva['descripcion']
            request.user.extesionusuario.red_social=data_nueva['red_social']
            request.user.extesionusuario.save()
            request.user.save()
            return redirect('perfil_del_usuario')
    else:        
        formulario=EditarPerfilDeUsuario(initial={'first_name':request.user.first_name, 'last_name':request.user.last_name, 'email':request.user.email,'avatar':request.user.extesionusuario.avatar, 'descripcion':request.user.extesionusuario.descripcion,'red_social':request.user.extesionusuario.red_social, })
    return render(request, 'accounts/editar_perfil.html',{'formulario':formulario})

class CambiarLlave(LoginRequiredMixin, PasswordChangeView):
    template_name='accounts/cambiar_contaseña.html'
    success_url='/accounts/perfil_del_usuario'
    form_class=CambioDeContraseña