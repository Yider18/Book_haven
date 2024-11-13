from django.contrib.auth.models import User
from django.db import models

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    preferencias = models.CharField(max_length=200)  # Para almacenar preferencias de lectura

    def __str__(self):
        return self.usuario.username

