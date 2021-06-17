# accounts/views.py
from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.views import LoginView



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
 


