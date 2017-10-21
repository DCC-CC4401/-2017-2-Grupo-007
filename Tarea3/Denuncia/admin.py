from django.contrib import admin
from .models import Denuncia
import os

# Register your models here.

class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'estado', 'comuna', 'direccion', 'herido', 'persona', 'fecha')
    search_fields = ('tipo', 'estado', 'herido', 'persona')


admin.site.register(Denuncia, DenunciaAdmin)

