from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=180)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)

def __str__(selft):
    return f"{selft.nombre} - {selft.email}"
