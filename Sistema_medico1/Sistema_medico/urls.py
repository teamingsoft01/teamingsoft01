"""Sistema_medico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from Sistema_medico.views import *
from django.urls import path, include # new




urlpatterns = [

    path('admin/', admin.site.urls),
    path('index.html', index),
    path('iniciosesion.html', iniciodesesion),
    path('innerpage.html',innerpage),
    path('notamedica.html', notamedica),


    # path('sesiondoctor.html', sesiondoctor),
    # path('sesionpaciente.html',sesionpaciente),

    path('inventariomedicamento.html',inventariomedicamento),

    path('menu_principal.html', menu_principal),
    path('menu_paciente.html',menu_paciente),
    path('menu_doctor.html', menu_doctor),
    



   
    path('getPaciente.html', getPaciente),
    path("tablahistoriaclinica.html", getHitorial),

    path('historiaclinica.html', historiaClinica),

    path('accounts/', include('django.contrib.auth.urls')), # new
    path('accounts/', include('accounts.urls')), # new


    path('programarcitas.html', programarcitas),

    
]
