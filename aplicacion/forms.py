from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)