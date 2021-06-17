# Correr el servidor python manage.py runserver

# Request: Para realizar peticiones al servidor.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.
from typing import Text

from django.http import request
from Usuario_PostgreSQL.models import Agenda, Pacientes, Notamedica
from Usuario_PostgreSQL.models import HistorialClinicaPacientes
from Usuario_PostgreSQL.models import Medicamentos


from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from Sistema_medico import settings
from django.core.mail import send_mail






# esto es una vista


def index(request):  # pasamos un objecto de tipo request como primer argumento
    return render(request, 'index.html')


def iniciodesesion(request):
    return render(request, 'iniciosesion.html')


def innerpage(request):
    return render(request, 'inner-page.html')

def notamedica(request):
    if request.method == "POST":
            txtfechadeatencion = request.POST["fechadeatencion"]
            txtnombre = request.POST["nombre"]
            txtemailpaciente = request.POST["emailpaciente"]
            txtsubjetivo = request.POST["subjetivo"]
            txtobjetivo = request.POST["objetivo"]
            txtanalisis = request.POST["analisis"]
            txtplan = request.POST["plan"]
            nuevaNota = Notamedica.objects.create( fechadeatencion=txtfechadeatencion , nombre=txtnombre, emailpaciente=txtemailpaciente, subjetivo=txtsubjetivo, objetivo=txtobjetivo, analisis=txtanalisis, plan=txtplan) 
    return render(request, 'notamedica.html')

# def sesiondoctor(request):
#     return render(request, 'sesiondoctor.html')
# def sesionpaciente(request):
#     return render(request, 'registration/sesionpaciente.html')
# def historiaClinica(request):
#     return render(request, 'historiaclinica.html')





def inventariomedicamento(request):
    return render(request, 'inventariomedicamento.html')


def programarcitas(request):
    return render(request, 'programarcitas.html')



def menu_principal(request):
    return render(request, 'menu_principal.html')

def menu_paciente(request):
    return render(request, 'menu_paciente.html')

def menu_doctor(request):
    return render (request, 'menu_doctor.html')


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
    historialPacientes = HistorialClinicaPacientes.objects.all()
    # historialPacientes = HistorialClinicaPacientes.objects.filter(nombre__contains = 'Tristan')
    # historialPacientes = HistorialClinicaPacientes.objects.filter(nombrePaciente = 'Tristan' )
    return render(request, 'tablahistoriaclinica.html', {"Historial": historialPacientes})


def historiaClinica(request):
    if request.method == "POST":
            nombre = request.POST["txtnombre"]
            tipodesangre = request.POST['txttipodesangre'] 
            fechauem = request.POST["txtfechauem"]
            resultadospa =request.POST["txtresultadospa"] 
            enfermedadesmi = request.POST["txtenfermedadesmi"] 
            medicamentoa = request.POST["txtmedicamentoa"]
            alergias = request.POST["txtalergias"]
            enfermedadc = request.POST["txtenfermedadc"] 
            enfermedadcf =request.POST["txtenfermedadcf"]
            nuevoPaciente= HistorialClinicaPacientes.objects.create(nombrePaciente=nombre, tipoSangre=tipodesangre, fechaExamenMedico=fechauem, resultadoPrueba=resultadospa, enfermedadesImportantes=enfermedadesmi,  medicamentoActual=medicamentoa, enfermedadesCronicas=enfermedadc, alergias=alergias, enfermedadesCronicasFamiliares=enfermedadcf)
    return render(request, 'historiaclinica.html')

def programarcitas(request):
    if request.method == "POST":
            nombre = request.POST["nombre"]
            curp = request.POST["curp"]
            emailpaciente = request.POST['emailpaciente']
            fechadeatencion = request.POST['fechadeatencion']
            horadeatencion = request.POST['horadeatencion']
            nuevaAgenda = Agenda.objects.create(nombre=nombre, curp=curp, correo=emailpaciente, fechaAtencion=fechadeatencion, horaAtencion=horadeatencion)

            cita= request.POST["nombre"] + "/ Curp: " + request.POST["curp"] + "/ Correo " + request.POST['emailpaciente'] + "/ Fecha de atencion: " + request.POST['fechadeatencion'] + "/ Hora de atencion" + request.POST['horadeatencion']
            email_desde = settings.EMAIL_HOST_USER
            email_para =   emailpaciente
            send_mail(cita, email_desde, [email_para], fail_silently=False)

    return render(request,'programarcitas.html')


def inventariomedicamento(request):
    print(request.GET)
    queryset = request.GET.get("buscar")
    post = Medicamentos.objects.all()   
    if queryset:
        post = Medicamentos.objects.filter(
            Q(nombreMedicamento=queryset)
        ).distinct()
    return render(request, 'inventariomedicamento.html', {"Medicamento": post})




