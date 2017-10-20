from django.db import models

# Create your models here.
from django.db import models


class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    foto = models.CharField(max_length=200)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    fecha_ingreso = models.DateTimeField(max_length=50)
