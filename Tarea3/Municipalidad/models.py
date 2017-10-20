from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Municipalidad(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    foto = models.CharField(max_length=200)
    usuario = models.ForeignKey(User)


