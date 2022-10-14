from django.urls import path
from home import views

urlpatterns = [
    path('hola/', views.hola),
    path('', views.index),    
]