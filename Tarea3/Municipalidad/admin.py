from django.contrib import admin
from .models import Municipalidad


# Register your models here.

class MunicipalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comuna', 'direccion', 'usuario')
    search_fields = ('nombre', 'usuario')


admin.site.register(Municipalidad, MunicipalidadAdmin)
