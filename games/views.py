from django.shortcuts import redirect, render
from games.models import Videojuego
from games.forms import VideojuegoFormulario, BusquedaVideojuego
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class VerVideojuego(DetailView):
    
    model = Videojuego
    template_name = 'games/ver_videojuego.html'

def ver_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    formulario = BusquedaVideojuego()
    nombre=request.GET.get('nombre',None)
    if nombre:
        videojuegos=Videojuego.objects.filter(nombre__icontains=nombre)
    else:
        videojuegos=Videojuego.objects.all()
    return render(request, 'games/ver_videojuegos.html', {'videojuegos': videojuegos, 'formulario': formulario} )

class ListaVideojuegos(ListView):
    
    model = Videojuego
    template_name = 'games/lista_videojuegos.html'
    
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            videojuegos = self.model.objects.filter(nombre__icontains=nombre)
        else:
            videojuegos = self.model.objects.all()
        return videojuegos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaVideojuego()
        return context

class CrearVideojuego(LoginRequiredMixin,CreateView):
    model = Videojuego
    success_url = '/games/videojuegos/'
    template_name = 'games/crear_videojuego.html'
    fields = ['nombre', 'desarrollador', 'genero', 'plataformas', 'precio', 'jugadores', 'lanzamiento', 'distribuidor', 'descripcion', 'caratula', 'autor']

class EditarVideojuego(LoginRequiredMixin,UpdateView):
    model = Videojuego
    success_url = '/games/videojuegos/'
    template_name = 'games/editar_videojuego.html'
    fields = ['nombre', 'desarrollador', 'genero', 'plataformas', 'precio', 'jugadores', 'lanzamiento', 'distribuidor', 'descripcion', 'caratula', 'autor']
    
class EliminarVideojuego(LoginRequiredMixin,DeleteView):
    model = Videojuego
    success_url = '/games/videojuegos/'
    template_name = 'games/eliminar_videojuego.html'

