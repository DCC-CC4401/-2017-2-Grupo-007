# Create your models here.
from django.db import models
from Persona.models import Persona


class Denuncia(models.Model):
    estado = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    color = models.CharField(max_length=50)
    herido = models.CharField(max_length=2)
    persona = models.ForeignKey(Persona, null=True, blank=True)
