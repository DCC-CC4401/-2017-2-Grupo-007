from django.db import models
from ONG.models import ONG


class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos/', null=True)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    fecha_ingreso = models.DateTimeField(max_length=50)
    ong_responsable = models.ForeignKey(ONG, null=True)
