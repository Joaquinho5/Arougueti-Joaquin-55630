from django import forms

#Bolso
class BolsoForm(forms.Form):
    nombre = forms.CharField(max_length=200, required=True)
    codigo = forms.CharField(max_length=200, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
