from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    publicado_en = models.DateField()

    def __str__(self):
        return self.titulo

