from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExtesionUsuario(models.Model):

    avatar=models.ImageField(upload_to='avatares',null=True, blank=True)
    descripcion = models.CharField(null=True,max_length=50)
    red_social= models.CharField(null=True,max_length=200)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
class ExtesionUsuario2(models.Model):
    ...
