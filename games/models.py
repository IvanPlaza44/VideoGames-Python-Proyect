from django.db import models
from ckeditor.fields import RichTextField


class Videojuego(models.Model):
    nombre = models.CharField(max_length=30)
    desarrollador = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    plataformas = models.CharField(max_length=30)
    precio = models.IntegerField()
    jugadores = models.IntegerField()
    lanzamiento = models.DateField()
    distribuidor = models.CharField(max_length=30)
    descripcion = RichTextField(null=True)
    caratula = models.ImageField(upload_to= 'avatares', null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre}'