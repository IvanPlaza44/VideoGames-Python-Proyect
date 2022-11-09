from django.shortcuts import redirect, render
from games.models import Videojuego
from games.forms import VideojuegoFormulario
from games.forms import BusquedaVideojuegos

def ver_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    formulario=BusquedaVideojuegos()
    return render(request, 'games/ver_videojuegos.html', {'videojuegos':videojuegos, 'formulario':formulario} )

def crear_videojuegos(request):
    
    if request.method == 'POST':
        formulario = VideojuegoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            videojuego = Videojuego(
                        nombre = datos['nombre'],
                        desarrollador = datos['desarrollador'], 
                        genero = datos['genero'], 
                        plataformas = datos['plataformas'], 
                        precio = datos['precio'], 
                        jugadores = datos['jugadores'], 
                        lanzamiento = datos['lanzamiento'], 
                        resumen = datos['resumen']
            )
            videojuego.save()
            return redirect('ver_videojuegos')
    
    formulario = VideojuegoFormulario()
    
    return render(request, 'games/crear_videojuegos.html', {'formulario': formulario})


