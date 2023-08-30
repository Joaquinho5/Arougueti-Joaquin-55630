from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def base(request):
    return render(request, "aplicacion/base.html")

# Gorros
def gorro(request):
    contexto = {'Gorros': Gorro.objects.all()}
    return render(request, "aplicacion/gorro.html", contexto)


#Bolsos

def bolso(request):
    contexto = {'Bolsos': Bolso.objects.all()}
    return render(request, "aplicacion/bolso.html", contexto)




#Riñoneras

def rinionera(request):
    contexto = {'Rinioneras': Rinionera.objects.all()}
    return render(request, "aplicacion/rinionera.html", contexto)




#Guantes

def guante(request):
    contexto = {'Guantes': Guante.objects.all()}
    return render(request, "aplicacion/guante.html", contexto)
