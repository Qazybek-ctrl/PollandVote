from django.shortcuts import redirect, render
from .forms import PollCreateForm
from . import views_cases
from .models import Poll, Voted

def poll_creation_view(request):
    context = {
        'form':PollCreateForm(),
        'active':request.user.is_authenticated
    }
    if request.user.is_authenticated == False:
        return redirect('error2') 
    elif request.method == "POST":
        return views_cases.poll_creation(request)
    return render(request, 'Content/poll_creation.html', context)

def home(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, 'Content/home.html', context)

def start_poll_view(request):
    context = {
        'active':request.user.is_authenticated
    }
    if request.method == 'GET'and 'poll_id' in request.GET:
        return views_cases.check_user_validity(request)
    elif request.method == 'POST':
        return views_cases.user_voting(request)
    return render(request, 'Content/poll_begin.html', context)

def polls(request):
    context = views_cases.polls_view_data_preparation(request)
    if request.method == 'POST':
        poll_id = request.POST['poll_id']
        poll = Poll.objects.get(id=poll_id)
        poll.delete()
    if request.method == 'GET' and 'query' in request.GET:
        context['polls'] = Poll.objects.filter(category=request.GET['query'])
    return render(request, "Content/polls.html", context)

def accepted_poll_view(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, "Content/succeed.html", context)

def second_vote_view(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, "Content/error.html", context)

def third_vote_view(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, "Content/error2.html", context)