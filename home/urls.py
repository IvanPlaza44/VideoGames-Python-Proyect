from django.urls import path
from home import views

urlpatterns = [
    path('acerca_de_nosotros/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
    path('', views.index, name='index'),    
]