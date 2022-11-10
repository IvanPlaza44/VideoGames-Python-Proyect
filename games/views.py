from django.shortcuts import render
from games.models import Videojuego

def ver_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'ver_videojuegos.html', {'videojuegos': videojuegos})
