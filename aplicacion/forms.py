from django import forms

#Bolso
class BolsoForm(forms.Form):
    nombre = forms.CharField(max_length=200, required=True)
    codigo = forms.CharField(max_length=200, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

class GorroForm(forms.Form):
    nombre = forms.CharField(max_length=200, required=True)
    codigo = forms.CharField(max_length=200, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

class RinioneraForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    codigo = forms.CharField(max_length=200)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class GuanteForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    codigo = forms.CharField(max_length=200)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)