from contextvars import Context
from django.shortcuts import render

def acerca_de_nosotros(request):
    return render(request,'home/acerca_de_nosotros.html',{})

def index(request):
    return render(request, 'home/index.html')

