from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar_sesion/',views.iniciar_sesion,name='iniciar_sesion'),
    path('registrar/',views.registrar,name='registrar'),
    path('perfil_del_usuario/',views.mi_perfil,name='perfil_del_usuario'),
    path('cerrar_sesion/',LogoutView.as_view(template_name='accounts/cerrar_sesion.html'),name="cerrar_sesion"),
]
