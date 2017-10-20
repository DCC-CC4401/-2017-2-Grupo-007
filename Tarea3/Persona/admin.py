from django.contrib import admin
from .models import Persona


# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'sexo', 'email', 'fono', 'usuario')
    search_fields = ('rut', 'nombre', 'sexo', 'usuario')


admin.site.register(Persona, PersonaAdmin)
