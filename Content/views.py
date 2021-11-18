from django.shortcuts import redirect, render
from . import views_cases
from .models import Poll, Voted



def home(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, 'Content/home.html', context)

def start_poll_view(request):
    context = {}
    if request.method == 'GET'and 'poll_id' in request.GET:
        return views_cases.check_user_validity(request)
    elif request.method == 'POST':
        return views_cases.user_voting(request)
    return render(request, 'Content/poll_begin.html', context)

def polls(request):
    context = views_cases.polls_view_data_preparation(request)
    return render(request, "Content/polls.html", context)

def accepted_poll_view(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, "Content/succeed.html", context)

def second_vote_view(request):
    return render(request, "Content/error.html")