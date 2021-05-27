from django.contrib import admin
from .models import Pacientes
# Register your models here.


class PacienteAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display=('id', 'nombre', 'curp','nss')


# admin.site.register(Pacientes)
admin.site.register(Pacientes, PacienteAdmin)
