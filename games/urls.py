from django.urls import path 
from  games import views

urlpatterns = [
    path('videojuegos/', views.ver_videojuegos, name='ver_videojuegos'),
    path('videojuegos/crear', views.crear_videojuegos, name='crear_videojuegos')

]
