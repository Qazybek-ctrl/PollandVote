from django.http import request
from django.shortcuts import redirect, render

from .forms import RegForm

from . import views_cases
# Create your views here.

def logining_view(request):
    return render(request, 'Auth/logining.html')

def registration_view(request):
    context = {
        'forms':RegForm(),
        'error':''
    }
    if request.method == 'POST':
        context['error'] = views_cases.check_user_unique(request)
        if context['error'] == '':
            return redirect("auth")
    return render(request, 'Auth/registration.html', context)