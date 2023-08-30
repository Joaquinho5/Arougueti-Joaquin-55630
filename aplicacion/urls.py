from django.urls import path, include
from .views import *

urlpatterns = [
    # Base
    path('', base, name="base"),

    # Gorros
    path('gorros/', gorro, name="gorro"),

    #Bolsos
    path('bolsos/', bolso, name="bolso"),

    #Riñoneras
    path('riñoneras/', rinionera, name="rinionera"),

    #Guantes
    path('guantes/', guante, name="guante"),
    
]