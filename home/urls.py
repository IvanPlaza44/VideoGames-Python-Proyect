from django.urls import path
from home import views

urlpatterns = [
    path('acerca_de_nosotros/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
    path('ver_usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('usuario_creado/', views.usuario_creado, name='usuario_creado'),
    path('', views.index, name='index'),    
]