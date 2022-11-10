from django.urls import path
from games import views
urlpatterns = [
    path('games/', views.ver_videojuegos, name='ver_videojuegos')
]
