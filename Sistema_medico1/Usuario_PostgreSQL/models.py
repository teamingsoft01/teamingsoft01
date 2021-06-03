from django.db import models

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
