from django.urls import path
from games import views
urlpatterns = [
    path('videojuegos/', views.ver_videojuegos, name='ver_videojuegos'),        
    path('videojuegos/', views.ListaVideojuegos.as_view(), name='ver_videojuegos'),
    path('videojuegos/crear', views.CrearVideojuego.as_view(), name='crear_videojuego'),
    path('videojuegos/editar/<int:pk>', views.EditarVideojuego.as_view(), name='editar_videojuego'),
    path('videojuegos/eliminar/<int:pk>', views.EliminarVideojuego.as_view(), name='eliminar_videojuego'),
    #path('videojuegos/ver/<int:pk>', views.VerVideojuego.as_view(), name='ver_videojuego')
]
