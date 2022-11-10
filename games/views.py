from django.shortcuts import redirect, render
from games.models import Videojuego
from games.forms import VideojuegoFormulario
from games.forms import BusquedaVideojuegos

def ver_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    formulario=BusquedaVideojuegos()
    return render(request, 'games/ver_videojuegos.html', {'videojuegos':videojuegos, 'formulario':formulario} )

def crear_videojuego(request):
    
    if request.method == 'POST':
        formulario = VideojuegoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            videojuego = Videojuego(
                        nombre = datos['nombre'],
                        desarrollador = datos['desarrollador'], 
                        genero = datos['genero'], 
                        plataformas = datos['plataformas'],                         
                        jugadores = datos['jugadores'], 
                        lanzamiento = datos['lanzamiento'], 
                        resumen = datos['resumen']
            )
            videojuego.save()
            return redirect('ver_videojuegos')
        else:
           return render(request, 'games/crear_videojuego.html', {'formulario': formulario}) 
    formulario = VideojuegoFormulario()
    
    return render(request, 'games/crear_videojuego.html', {'formulario': formulario})


def editar_videojuego(request, id):
    
    videojuego = Videojuego.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = VideojuegoFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            videojuego.nombre = datos['nombre'],
            videojuego.desarrollador = datos['desarrollador'], 
            videojuego.genero = datos['genero'], 
            videojuego.plataformas = datos['plataformas'],              
            videojuego.jugadores = datos['jugadores'], 
            videojuego.lanzamiento = datos['lanzamiento'], 
            videojuego.resumen = datos['resumen']
            
            videojuego.save()
            return redirect('ver_videojuegos')
        
    
    formulario = VideojuegoFormulario(
        initial={
            'nombre': videojuego.nombre, 
            'desarrollador': videojuego.desarrollador,  
            'genero': videojuego.genero, 
            'plataformas': videojuego.plataformas,             
            'jugadores': videojuego.jugadores, 
            'lanzamiento': videojuego.lanzamiento, 
            'resumen': videojuego.resumen
        }
    )
    
    return render(request, 'games/editar_videojuego.html', {'formulario': formulario, 'videojuego': videojuego})

def eliminar_videojuego(request, id):
    
    videojuego = Videojuego.objects.get(id=id)
    videojuego.delete()
    return redirect('ver_videojuegos')