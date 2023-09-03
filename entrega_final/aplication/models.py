from django.db import models
from django.contrib.auth.models import User


class Posteo(models.Model):
    titulo = models.CharField(max_length=200,blank=True, null=True)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=200,blank=True, null=True)
    categorias = models.CharField(max_length=200,blank=True, null=True)
    

    def __str__(self):
        return self.titulo

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.usuario.username

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"

