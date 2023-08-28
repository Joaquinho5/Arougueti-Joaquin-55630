from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    publicacion = models.ForeignKey('Publicacion', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentario por {self.usuario.username} en {self.publicacion.titulo}'


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()
    lugares_visitados = models.TextField()
    publicaciones_favoritas = models.ManyToManyField('Publicacion', blank=True)
    # Otros campos relacionados con el perfil de usuario

    def __str__(self):
        return self.usuario.username