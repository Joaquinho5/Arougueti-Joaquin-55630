from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Base y about me
    path('', base, name="base"),
    path('about/', about, name='about'),

    # Log in / log out / registro / editar perfil
    path('login/', login_request, name="login" ),
    path('registro/', register, name="registro" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),

    # Gorros

    path('gorros/', gorro, name="gorro"),
    path('updateGorro/<id_gorro>/', updateGorro, name="updateGorro"),
    path('deleteGorro/<id_gorro>/', deleteGorro, name="deleteGorro"),
    path('createGorro/', createGorro, name="createGorro"),
    path('buscar_gorro/', buscarGorro, name="buscar_gorro" ),
    path('buscar/', buscar, name="buscar" ),

    #Bolsos

    path('bolsos/', bolso, name="bolso"),
    path('updateBolso/<id_bolso>/', updateBolso, name="updateBolso"),
    path('deleteBolso/<id_bolso>/', deleteBolso, name="deleteBolso"),
    path('createBolso/', createBolso, name="createBolso"),
    path('buscar_bolso/', buscarBolso, name="buscar_bolso" ),
    path('buscar2/', buscar2, name="buscar2" ),

    #Riñoneras

    path('riñoneras/', rinionera, name="rinionera"),
    path('updateRinionera/<id_rinionera>/', updateRinionera, name="updateRinionera"),
    path('deleteRinionera/<id_rinionera>/', deleteRinionera, name="deleteRinionera"),
    path('createRinionera/', createRinionera, name="createRinionera"),
    path('buscar_rinionera/', buscarRinionera, name="buscar_rinionera" ),
    path('buscar3/', buscar3, name="buscar3" ),

    #Guantes
    
    path('guantes/', guante, name="guante"),
    path('updateGuante/<id_guante>/', updateGuante, name="updateGuante"),
    path('deleteGuante/<id_guante>/', deleteGuante, name="deleteGuante"),
    path('createGuante/', createGuante, name="createGuante"),
    path('buscar_guantes/', buscarGuante, name="buscar_guante" ),
    path('buscar4/', buscar4, name="buscar4" ),
    
]