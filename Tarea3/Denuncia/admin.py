from django.contrib import admin
from .models import Denuncia


# Register your models here.

class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'estado', 'lugar', 'herido', 'persona')
    search_fields = ('tipo', 'estado', 'herido', 'persona')


admin.site.register(Denuncia, DenunciaAdmin)
