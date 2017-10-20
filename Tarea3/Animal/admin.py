from django.contrib import admin
from .models import Animal


# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre', 'sexo', 'edad', 'fecha_ingreso')
    search_fields = ('tipo', 'sexo', 'edad', 'fecha_ingreso')


admin.site.register(Animal, AnimalAdmin)
