# Create your models here.
from django.db import models
from Persona.models import Persona
from django.utils import timezone
from utils.choices import tipoAnimal, sexoChoice, colorChoice, heridoChoice, comunaChoice, estadoChoice


class Denuncia(models.Model):
    estado = models.CharField(
        choices= estadoChoice,
        max_length=50,
        default='RE')
    comuna= models.CharField(
        choices=comunaChoice,
        max_length=50,
        default='SA'

    )
    direccion = models.CharField(max_length=50)
    tipo = models.CharField(
        choices=tipoAnimal,
        max_length=50
    )
    sexo = models.CharField(
        choices=sexoChoice,
        max_length=50
    )
    color = models.CharField(
        choices=colorChoice,
        max_length=50
    )
    herido = models.CharField(
        choices=heridoChoice,
        max_length=50
    )
    persona = models.ForeignKey(Persona, null=True, blank=True)
    fecha = models.DateTimeField(default=timezone.now)
