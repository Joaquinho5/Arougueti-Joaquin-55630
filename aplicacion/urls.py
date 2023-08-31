from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Base
    path('', base, name="base"),

    # Log in / log out / registro
    path('login/', login_request, name="login" ),
    path('registro/', register, name="registro" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),


    # Gorros
    path('gorros/', gorro, name="gorro"),
    path('updateGorro/<id_gorro>/', updateGorro, name="updateGorro"),
    path('deleteGorro/<id_gorro>/', deleteGorro, name="deleteGorro"),
    path('createGorro/', createGorro, name="createGorro"),
    #Bolsos
    path('bolsos/', bolso, name="bolso"),
    path('updateBolso/<id_bolso>/', updateBolso, name="updateBolso"),
    path('deleteBolso/<id_bolso>/', deleteBolso, name="deleteBolso"),
    path('createBolso/', createBolso, name="createBolso"),

    #Riñoneras
    path('riñoneras/', rinionera, name="rinionera"),
    path('updateRinionera/<id_rinionera>/', updateRinionera, name="updateRinionera"),
    path('deleteRinionera/<id_rinionera>/', deleteRinionera, name="deleteRinionera"),
    path('createRinionera/', createRinionera, name="createRinionera"),

    #Guantes
    path('guantes/', guante, name="guante"),
    path('updateGuante/<id_guante>/', updateGuante, name="updateGuante"),
    path('deleteGuante/<id_guante>/', deleteGuante, name="deleteGuante"),
    path('createGuante/', createGuante, name="createGuante"),
    
]