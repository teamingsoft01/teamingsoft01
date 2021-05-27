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