from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def base(request):
    return render(request, "aplicacion/base.html")