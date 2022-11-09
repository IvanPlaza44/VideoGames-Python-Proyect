from unittest.util import _MAX_LENGTH
from urllib import request
from django.db import models

# Create your models here.
class Videojuego(models.Model):
    nombre = models.CharField(max_length=40)
    desarrollador = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    plataformas = models.CharField(max_length=40)
    precio = models.IntegerField()
    jugadores = models.CharField(max_length=40)
    lanzamiento = models.DateField()
    resumen = models.CharField(max_length=40)
    
def __str__(self):
    return f'{self.nombre} {self.desarrollador}'