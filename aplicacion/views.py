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

def updateGorro(request, id_gorro):
    gorro = Gorro.objects.get(id=id_gorro)
    if request.method == "POST":
        miForm = GorroForm(request.POST)
        if miForm.is_valid():
            gorro.nombre = miForm.cleaned_data.get('nombre')
            gorro.codigo = miForm.cleaned_data.get('codigo')
            gorro.precio = miForm.cleaned_data.get('precio')
            gorro.save()
            return redirect(reverse_lazy('gorro'))   
    else:
        miForm = GorroForm(initial={
            'nombre': gorro.nombre,
            'codigo': gorro.codigo,
            'precio': gorro.precio,
        })
    return render(request, "aplicacion/gorroForm.html", {'form': miForm})

def deleteGorro(request, id_gorro):
    gorro = Gorro.objects.get(id=id_gorro)
    gorro.delete()
    return redirect(reverse_lazy('gorro'))

def createGorro(request):    
    if request.method == "POST":
        miForm = GorroForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_codigo = miForm.cleaned_data.get('codigo')
            p_precio = miForm.cleaned_data.get('precio')
            gorro = Gorro(nombre=p_nombre, 
                             codigo=p_codigo,
                             precio=p_precio,
                             )
            gorro.save()
            return redirect(reverse_lazy('gorro'))
    else:
        miForm = GorroForm()

    return render(request, "aplicacion/gorroForm.html", {"form":miForm})


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

def updateRinionera(request, id_rinionera):
    rinionera = Rinionera.objects.get(id=id_rinionera)
    if request.method == "POST":
        miForm = RinioneraForm(request.POST)
        if miForm.is_valid():
            rinionera.nombre = miForm.cleaned_data.get('nombre')
            rinionera.codigo = miForm.cleaned_data.get('codigo')
            rinionera.precio = miForm.cleaned_data.get('precio')
            rinionera.save()
            return redirect(reverse_lazy('rinionera'))   
    else:
        miForm = RinioneraForm(initial={
            'nombre': rinionera.nombre,
            'codigo': rinionera.codigo,
            'precio': rinionera.precio,
        })
    return render(request, "aplicacion/rinioneraForm.html", {'form': miForm})

def deleteRinionera(request, id_rinionera):
    rinionera = Rinionera.objects.get(id=id_rinionera)
    rinionera.delete()
    return redirect(reverse_lazy('rinionera'))

def createRinionera(request):    
    if request.method == "POST":
        miForm = RinioneraForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_codigo = miForm.cleaned_data.get('codigo')
            p_precio = miForm.cleaned_data.get('precio')
            rinionera = Rinionera(nombre=p_nombre, 
                             codigo=p_codigo,
                             precio=p_precio,
                             )
            rinionera.save()
            return redirect(reverse_lazy('rinionera'))
    else:
        miForm = RinioneraForm()

    return render(request, "aplicacion/rinioneraForm.html", {"form":miForm})

#Guantes

def guante(request):
    contexto = {'Guantes': Guante.objects.all()}
    return render(request, "aplicacion/guante.html", contexto)

def updateGuante(request, id_guante):
    guante = Guante.objects.get(id=id_guante)
    if request.method == "POST":
        miForm = GuanteForm(request.POST)
        if miForm.is_valid():
            guante.nombre = miForm.cleaned_data.get('nombre')
            guante.codigo = miForm.cleaned_data.get('codigo')
            guante.precio = miForm.cleaned_data.get('precio')
            guante.save()
            return redirect(reverse_lazy('guante'))   
    else:
        miForm = GuanteForm(initial={
            'nombre': guante.nombre,
            'codigo': guante.codigo,
            'precio': guante.precio,
        })
    return render(request, "aplicacion/guanteForm.html", {'form': miForm})

def deleteGuante(request, id_guante):
    guante = Guante.objects.get(id=id_guante)
    guante.delete()
    return redirect(reverse_lazy('guante'))

def createGuante(request):    
    if request.method == "POST":
        miForm = GuanteForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_codigo = miForm.cleaned_data.get('codigo')
            p_precio = miForm.cleaned_data.get('precio')
            guante = Guante(nombre=p_nombre, 
                             codigo=p_codigo,
                             precio=p_precio,
                             )
            guante.save()
            return redirect(reverse_lazy('guante'))
    else:
        miForm = RinioneraForm()

    return render(request, "aplicacion/guanteForm.html", {"form":miForm})
