from django.urls import path 
from  games import views

urlpatterns = [
    path('videojuegos/', views.ver_videojuegos, name='ver_videojuegos'),
    path('videojuegos/crear', views.crear_videojuego, name='crear_videojuego'),
    path('videojuegos/editar/<int:id>', views.editar_videojuego, name='editar_videojuego')

]
