
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'register/register.html')


def registered(request):
    return render(request, 'register/registration_done.html')
