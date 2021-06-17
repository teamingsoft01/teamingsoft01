from django.http import HttpResponse
from django.shortcuts import redirect

def user(view_func):
    def wrapper_fun(request, *args, **kwargs):
        
        return view_func(request, *args, **kwargs)
    return wrapper_fun