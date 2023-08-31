from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import *
from .forms import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.db.models import Q


def base(request):
    return render(request, "aplicacion/base.html")

def about(request):
    return render(request, 'aplicacion/aboutme.html')

## Login / log out / registro

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                    
                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a este bello sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos no válidos querido'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos no válidos querido'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm}) 

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
  
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })

## Gorros

@login_required
def gorro(request):
    contexto = {'Gorros': Gorro.objects.all()}
    return render(request, "aplicacion/gorro.html", contexto)

@login_required
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

@login_required
def deleteGorro(request, id_gorro):
    gorro = Gorro.objects.get(id=id_gorro)
    gorro.delete()
    return redirect(reverse_lazy('gorro'))

@login_required
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

@login_required
def buscarGorro(request):
    return render(request, "aplicacion/buscarGorro.html")

@login_required
def buscar(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        Gorros = Gorro.objects.filter(Q(nombre__icontains=patron) | Q(codigo__icontains=patron))
        contexto = {"Gorros": Gorros, 'titulo': f'Cursos que tiene como patron "{patron}"'}
        return render(request, "aplicacion/gorro.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")


## Bolsos

@login_required
def bolso(request):
    contexto = {'Bolsos': Bolso.objects.all()}
    return render(request, "aplicacion/bolso.html", contexto)

@login_required
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

@login_required
def deleteBolso(request, id_bolso):
    bolso = Bolso.objects.get(id=id_bolso)
    bolso.delete()
    return redirect(reverse_lazy('bolso'))

@login_required
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

@login_required
def buscarBolso(request):
    return render(request, "aplicacion/buscarBolso.html")
    
@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        Bolsos = Bolso.objects.filter(Q(nombre__icontains=patron) | Q(codigo__icontains=patron))
        contexto = {"Bolsos": Bolsos, 'titulo': f'Bolsos que tiene como patron "{patron}"'}
        return render(request, "aplicacion/bolso.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")



## Riñoneras

@login_required
def rinionera(request):
    contexto = {'Rinioneras': Rinionera.objects.all()}
    return render(request, "aplicacion/rinionera.html", contexto)

@login_required
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

@login_required
def deleteRinionera(request, id_rinionera):
    rinionera = Rinionera.objects.get(id=id_rinionera)
    rinionera.delete()
    return redirect(reverse_lazy('rinionera'))

@login_required
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

@login_required
def buscarRinionera(request):
    return render(request, "aplicacion/buscarRinionera.html")
    
@login_required
def buscar3(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        Rinioneras = Rinionera.objects.filter(Q(nombre__icontains=patron) | Q(codigo__icontains=patron))
        contexto = {"Rinioneras": Rinioneras, 'titulo': f'Rinioneras que tiene como patron "{patron}"'}
        return render(request, "aplicacion/rinionera.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

## Guantes

@login_required
def guante(request):
    contexto = {'Guantes': Guante.objects.all()}
    return render(request, "aplicacion/guante.html", contexto)

@login_required
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

@login_required
def deleteGuante(request, id_guante):
    guante = Guante.objects.get(id=id_guante)
    guante.delete()
    return redirect(reverse_lazy('guante'))

@login_required
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

@login_required
def buscarGuante(request):
    return render(request, "aplicacion/buscarGuante.html")
    
@login_required
def buscar4(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        Guantes = Guante.objects.filter(Q(nombre__icontains=patron) | Q(codigo__icontains=patron))
        contexto = {"Guantes": Guantes, 'titulo': f'Guantes que tiene como patron "{patron}"'}
        return render(request, "aplicacion/guante.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")


