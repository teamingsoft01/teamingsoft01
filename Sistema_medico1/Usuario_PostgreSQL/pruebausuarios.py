from django.db.models.query_utils import Q
from Usuario_PostgreSQL.models import HistorialClinicaPacientes

nombre= (f'\'{"saul"}\'') 
tipo = (f'\'{"saul"}\'') 
fechaE=(f'\'{"saul"}\'') 
resultadop =(f'\'{"saul"}\'')  
enfermedadesI=(f'\'{"saul"}\'') 
medicamentoA =(f'\'{"saul"}\'') 
enfermedadesC= (f'\'{"saul"}\'') 
aler =(f'\'{"saul"}\'') 
enfermedadesCf=(f'\'{"saul"}\'') 

print(nombre)

# nuevoPaciente = HistorialClinicaPacientes( nombrePaciente= nombre,tipoSangre =tipo, fechaExamenMedico=fechaE,resultadoPrueba =resultadop, enfermedadesImportantes=enfermedadesI, medicamentoActual =medicamentoA,    enfermedadesCronicas=enfermedadesC, alergias =aler, enfermedadesCronicasFamiliares= enfermedadesC)


# nuevoPaciente.save()

# nuevoPaciente = HistorialClinicaPacientes.objects.create( nombrePaciente= 'saul', tipoSangre ='saul', fechaExamenMedico='saul', resultadoPrueba ='saul', enfermedadesImportantes='saul', medicamentoActual ='saul', enfermedadesCronicas='saul', alergias ='saul',enfermedadesCronicasFamiliares= 'saul')

nuevoPaciente = HistorialClinicaPacientes.objects.create(Q( nombrePaciente= f'{nombre}', tipoSangre =f'{tipo}', fechaExamenMedico=f'{fechaE}', resultadoPrueba =f'{resultadop}', enfermedadesImportantes=f'{enfermedadesI}', medicamentoActual =f'{medicamentoA}', enfermedadesCronicas=f'{enfermedadesC}', alergias =f'{aler}',enfermedadesCronicasFamiliares= f'{enfermedadesCf}'))
