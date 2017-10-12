from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    email = models.EmailField()
    fono = models.CharField(20)
    sexo = models.CharField(max_length=2)
    usuario = models.ForeignKey(User)


