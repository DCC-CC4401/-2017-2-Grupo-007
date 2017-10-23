from django.db import models
from django.contrib.auth.models import User
from utils.choices import sexoPersonaChoices


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    email = models.EmailField()
    fono = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=sexoPersonaChoices)
    usuario = models.ForeignKey(User)
    foto = models.ImageField(upload_to='fotos/', null=True)


