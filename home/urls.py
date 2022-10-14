from django.urls import path
from home import views

urlpatterns = [
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('hola/', views.hola),
    path('', views.index),    
]