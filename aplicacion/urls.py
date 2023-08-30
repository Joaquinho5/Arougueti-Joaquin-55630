from django.urls import path, include
from .views import *

urlpatterns = [
    # Base
    path('', base, name="base"),

    # Gorros
    path('gorros/', gorro, name="gorro"),

    #Bolsos
    path('bolsos/', bolso, name="bolso"),
    path('updateBolso/<id_bolso>/', updateBolso, name="updateBolso"),
    path('deleteBolso/<id_bolso>/', deleteBolso, name="deleteBolso"),
    path('createBolso/', createBolso, name="createBolso"),

    #Riñoneras
    path('riñoneras/', rinionera, name="rinionera"),

    #Guantes
    path('guantes/', guante, name="guante"),
    
]