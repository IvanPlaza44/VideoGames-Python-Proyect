from django.db import models
from ckeditor.fields import RichTextField

from datetime import datetime
# Create your models here.

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
    autor =models.CharField(max_length=30, null=True)
    fecha_de_creacion= models.DateTimeField(auto_now_add=True, null= True)
    
    def __str__(self):
        return f'{self.nombre}'