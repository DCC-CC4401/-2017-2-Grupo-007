from django.contrib import admin
from .models import ONG


# Register your models here.

class ONGAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'usuario')
    search_fields = ('nombre', 'usuario')


admin.site.register(ONG, ONGAdmin)
