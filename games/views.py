from django.shortcuts import redirect, render
from games.models import Videojuego
from games.forms import VideojuegoFormulario
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



def ver_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'games/ver_videojuegos.html', {'videojuegos': videojuegos})

class ListaVideojuegos(ListView):
    model = Videojuego
    template_name = 'games/lista_videojuegos.html'

class CrearVideojuego(LoginRequiredMixin,CreateView):
    model = Videojuego
    success_url = '/games/videojuegos/'
    template_name = 'games/crear_videojuego.html'
    fields = ['nombre', 'desarrollador', 'genero', 'plataformas', 'precio', 'jugadores', 'lanzamiento', 'distribuidor', 'descripcion']

class EditarVideojuego(LoginRequiredMixin,UpdateView):
    model = Videojuego
    success_url = '/games/videojuegos/'
    template_name = 'games/editar_videojuego.html'
    fields = ['nombre', 'desarrollador', 'genero', 'plataformas', 'precio', 'jugadores', 'lanzamiento', 'distribuidor', 'descripcion']
    
class EliminarVideojuego(LoginRequiredMixin,DeleteView):
    model = Videojuego
    success_url = '/games/videojuegos/'
    template_name = 'games/eliminar_videojuego.html'

class VerVideojuego(DetailView):
    model = Videojuego
    template_name = 'games/ver_videojuego.html'