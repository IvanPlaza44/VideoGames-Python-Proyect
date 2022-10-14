from django.urls import path
from home import views

urlpatterns = [
    path('ver_usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('hola/', views.hola),
    path('', views.index),    
]