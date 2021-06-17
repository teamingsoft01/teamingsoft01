from django.contrib import admin
from .models import Agenda, Notamedica, Pacientes, HistorialClinicaPacientes, Medicamentos
# Register your models here.


class PacienteAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'nombre', 'curp', 'nss')


# class HistorialClinicaPacienteAdmin(admin.ModelAdmin):
#     ordering = ('id',)
#     list_display = ('id', 'nombrePaciente','tipoSangre ',
#      'fechaExamenMedico', 'resultadoPrueba ', 'enfermedadesImportantes', 
#      'medicamentoActual', 'enfermedadesCronicas', 'alergias', 
#      'enfermedadesCronicasFamiliares')


# admin.site.register(Pacientes)
admin.site.register(Pacientes, PacienteAdmin)
admin.site.register(HistorialClinicaPacientes)

admin.site.register(Medicamentos)
admin.site.register(Agenda)
admin.site.register(Notamedica)
