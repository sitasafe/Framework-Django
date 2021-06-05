from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    publicado = models.DateTimeField("fecha de publicación")

def __str__(self):
    return self.curso_titulo


# Create your models here.
