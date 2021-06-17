from django.db import models
from django.db.models.base import Model

# Create your models here.


class Pacientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    nss = models.PositiveBigIntegerField()
    def __str__(self):
        texto = "{0} {1} {2} {3}"
        return texto.format(self.nombre, self.apellidos, self.curp, self.nss)


class HistorialClinicaPacientes(models.Model):
    nombrePaciente = models.CharField(max_length=150)
    tipoSangre = models.CharField(max_length=15)
    fechaExamenMedico = models.CharField(max_length=10)
    resultadoPrueba = models.CharField(max_length=50)
    enfermedadesImportantes = models.CharField(max_length=150)
    medicamentoActual = models.CharField(max_length=100)
    enfermedadesCronicas = models.CharField(max_length=150)
    alergias = models.CharField(max_length=100)
    enfermedadesCronicasFamiliares = models.CharField(max_length=100)
    def __str__(self):
        texto = "{0} {1} {2} {3} {4} {5} {6} {7} {8}"
        return texto.format(
            self.nombrePaciente, self.tipoSangre, self.fechaExamenMedico,
            self.resultadoPrueba, self.enfermedadesImportantes, self.medicamentoActual,
            self.enfermedadesCronicas, self.alergias, self.enfermedadesCronicasFamiliares)


class Medicamentos(models.Model):
    nombreMedicamento = models.CharField(max_length=30)
    costo = models.CharField(max_length=18)
    piezas = models.CharField(max_length=18)

    def __str__(self):
        texto = "{0} {1} {2}"
        return texto.format(self.nombreMedicamento, self.costo, self.piezas)

class Agenda(models.Model):
    nombre = models.CharField(max_length=120)
    curp = models.CharField(max_length=18)
    correo = models.CharField(max_length=50)
    fechaAtencion = models.CharField(max_length=10)
    horaAtencion= models.CharField(max_length=10)
    def __str__(self):
        texto = "{0} {1} {2} {3} {4}"
        return texto.format(self.nombre, self.curp, self.correo, self.fechaAtencion, self.horaAtencion)


class Notamedica(models.Model):
    fechadeatencion = models.CharField(max_length=18)
    nombre = models.CharField(max_length=120)
    emailpaciente= models.CharField(max_length=120)
    subjetivo= models.CharField(max_length=1000)
    objetivo= models.CharField(max_length=1000)
    analisis= models.CharField(max_length=1000)
    plan= models.CharField(max_length=1000)
    def __str__(self):
        texto = "{0} {1} {2} {3} {4} {5} {6}"
        return texto.format(
            self.fechadeatencion,
            self.nombre,
            self.emailpaciente, 
            self.subjetivo, 
            self.objetivo, 
            self.analisis, 
            self.plan
        )
