from django.http import request
from django.shortcuts import render

# Create your views here.

def logining_views(request):
    return render(request, 'Auth/logining.html')

def registration_views(request):
    return render(request, 'Auth/registration.html')