from contextvars import Context
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import Context, Template, loader

def hola(request):
    return HttpResponse("<h1>Hola, Bienvenidos a nuestro Blog</h1>")

def index(request):
    return render(request, 'home/index.html')

