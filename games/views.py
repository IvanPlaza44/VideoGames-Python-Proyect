from django.shortcuts import redirect, render
from games.models import Videojuego
from games.forms import VideojuegoFormulario
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def ver_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'games/ver_videojuegos.html', {'videojuegos': videojuegos})

class ListaVideojuegos(ListView):
    model = Videojuego
    template_name = 'games/lista_videojuegos.html'
    
class CrearVideojuego(CreateView):
    model = Videojuego
    success_url = '/games/videojuegos/'
    template_name = 'games/crear_videojuego.html'
    fields = ['nombre', 'desarrollador', 'genero', 'plataformas', 'precio', 'jugadores', 'lanzamiento', 'resumen']

class EditarVideojuego(UpdateView):
    model = Videojuego
    success_url = '/games/videojuegos/'
    template_name = 'games/editar_videojuego.html'
    fields = ['nombre', 'desarrollador', 'genero', 'plataformas', 'precio', 'jugadores', 'lanzamiento', 'resumen']
    
class EliminarVideojuego(DeleteView):
    model = Videojuego
    success_url = '/games/videojuegos/'
    template_name = 'games/eliminar_videojuego.html'