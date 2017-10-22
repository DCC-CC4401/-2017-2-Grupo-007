from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from utils.choices import comunaChoice

class Municipalidad(models.Model):
    nombre = models.CharField(max_length=50)
    comuna= models.CharField(
        max_length=50,
        choices = comunaChoice
    )
    direccion = models.CharField(max_length=50)
    foto = models.CharField(max_length=200)
    usuario = models.ForeignKey(User)


