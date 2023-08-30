from django.urls import path, include
from .views import *

urlpatterns = [
    # Base
    path('', base, name="base"),

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