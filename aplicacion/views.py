from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from .forms import *

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

def updateBolso(request, id_bolso):
    bolso = Bolso.objects.get(id=id_bolso)
    if request.method == "POST":
        miForm = BolsoForm(request.POST)
        if miForm.is_valid():
            bolso.nombre = miForm.cleaned_data.get('nombre')
            bolso.codigo = miForm.cleaned_data.get('codigo')
            bolso.precio = miForm.cleaned_data.get('precio')
            bolso.save()
            return redirect(reverse_lazy('bolso'))   
    else:
        miForm = BolsoForm(initial={
            'nombre': bolso.nombre,
            'codigo': bolso.codigo,
            'precio': bolso.precio,
        })
    return render(request, "aplicacion/bolsoForm.html", {'form': miForm})

def deleteBolso(request, id_bolso):
    bolso = Bolso.objects.get(id=id_bolso)
    bolso.delete()
    return redirect(reverse_lazy('bolso'))

def createBolso(request):    
    if request.method == "POST":
        miForm = BolsoForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_codigo = miForm.cleaned_data.get('codigo')
            p_precio = miForm.cleaned_data.get('precio')
            bolso = Bolso(nombre=p_nombre, 
                             codigo=p_codigo,
                             precio=p_precio,
                             )
            bolso.save()
            return redirect(reverse_lazy('bolso'))
    else:
        miForm = BolsoForm()

    return render(request, "aplicacion/bolsoForm.html", {"form":miForm})



#Riñoneras

def rinionera(request):
    contexto = {'Rinioneras': Rinionera.objects.all()}
    return render(request, "aplicacion/rinionera.html", contexto)




#Guantes

def guante(request):
    contexto = {'Guantes': Guante.objects.all()}
    return render(request, "aplicacion/guante.html", contexto)
