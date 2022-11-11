from unittest.util import _MAX_LENGTH
from urllib import request
from django.db import models

class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    correo_electronico=models.CharField(max_length=30)
    fecha_de_nacimiento=models.DateField()
    sexo=models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nombre} {self.apellido} Edad: {self.edad}' 