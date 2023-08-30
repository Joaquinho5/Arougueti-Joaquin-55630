from django.db import models
from django.contrib.auth.models import User

class Gorro(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"gorro: {self.nombre} y codigo: {self.codigo}"

class Bolso(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bolso: {self.nombre} y codigo: {self.codigo}"

class Rinionera(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Rinionera: {self.nombre} y codigo: {self.codigo}"

class Guante(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Rinionera: {self.nombre} y codigo: {self.codigo}"