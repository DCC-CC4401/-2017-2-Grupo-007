from django.contrib import admin
from .models import Municipalidad


# Register your models here.

class MunicipalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comuna', 'direccion', 'administrador')
    search_fields = ('nombre', 'administrador')


admin.site.register(Municipalidad, MunicipalidadAdmin)
