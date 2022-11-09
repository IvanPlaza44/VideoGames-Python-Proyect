from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.mi_login,name='login'),
    path('registrar/',views.registrar,name='registrar'),
    path('perfil_del_usuario/',views.mi_perfil,name='perfil_del_usuario'),
    path('perfil_del_usuario/editar', views.editar_perfil, name="editar_perfil"),
    path('cerrar_sesion/',LogoutView.as_view(template_name='accounts/cerrar_sesion.html'),name="cerrar_sesion"),
    path('perfil/cambiar_contraseña', views.CambiarLlave.as_view(), name="cambiar_contraseña")
]
