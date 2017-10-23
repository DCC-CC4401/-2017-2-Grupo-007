from django.contrib import admin
from .models import ONG


# Register your models here.

class ONGAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'administrador')
    search_fields = ('nombre', 'administrador')


admin.site.register(ONG, ONGAdmin)
