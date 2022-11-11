from django.db import models

# Create your models here.

class Videojuego(models.Model):
    nombre = models.CharField(max_length=30)
    desarrollador = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    plataformas = models.CharField(max_length=30)
    precio = models.IntegerField()
    jugadores = models.IntegerField()
    lanzamiento = models.DateField()
    resumen = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} -- {self.desarrollador} '