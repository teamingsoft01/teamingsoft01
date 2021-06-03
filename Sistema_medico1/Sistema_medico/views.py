# Correr el servidor python manage.py runserver

# Request: Para realizar peticiones al servidor.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.
from Usuario_PostgreSQL.models import Pacientes
from Usuario_PostgreSQL.models import HistorialClinicaPacientes
from Usuario_PostgreSQL.models import Medicamentos


from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q


# esto es una vista


def index(request):  # pasamos un objecto de tipo request como primer argumento
    return render(request, 'index.html')


def iniciodesesion(request):
    return render(request, 'iniciosesion.html')


def innerpage(request):
    return render(request, 'inner-page.html')


def sesiondoctor(request):
    return render(request, 'sesiondoctor.html')


def sesionpaciente(request):
    return render(request, 'registration/sesionpaciente.html')


def historiaClinica(request):
    return render(request, 'historiaclinica.html')


def inventariomedicamento(request):
    return render(request, 'inventariomedicamento.html')


def getPaciente(request):
    pacientesListados = Pacientes.objects.all()  # --> listar todos los valores
    # pacientesListados = Pacientes.objects.all()[:2] # --> listar solo un determinado numero de valores
    # pacientesListados = Pacientes.objects.all()[2:6] # --> listar desde un reango determinado
    # pacientesListados = Pacientes.objects.all().order_by('nombre') # --> listar por ordenamiento de alfabeto ascendente
    # pacientesListados = Pacientes.objects.all().order_by('-nombre') # --> listar por ordenamiento de alfabeto descendente
    # pacientesListados = Pacientes.objects.filter(nombre='Alan') # --> filtrar
    # pacientesListados = Pacientes.objects.filter(nombre__startswith='B') # --> filtar el nombre con la inicial
    # --> listar los valores que contengan alguna letra en especial
    # pacientesListados = Pacientes.objects.filter(nombre__contains='a')
    return render(request, 'getPaciente.html', {"Paciente": pacientesListados})

# def login(request):
#     # return render(request, 'registration/login.html')


def getHitorial(request):
    # historialPacientes = HistorialClinicaPacientes.objects.all()
    # historialPacientes = HistorialClinicaPacientes.objects.filter(nombre__contains = 'Tristan')
    historialPacientes = HistorialClinicaPacientes.objects.filter(nombrePaciente = 'Tristan' )
    return render(request, 'tablahistoriaclinica.html', {"Historial": historialPacientes})


def inventariomedicamento(request):
    print(request.GET)
    queryset = request.GET.get("buscar")
    post = Medicamentos.objects.all()
    if queryset:
        post = Medicamentos.objects.filter(
            Q(nombreMedicamento=queryset)
        ).distinct()
    return render(request, 'inventariomedicamento.html', {"Medicamento": post})

