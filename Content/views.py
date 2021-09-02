from django.shortcuts import render
from . import views_cases
from .models import Poll
# Create your views here.
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
        poll_id = request.GET['poll_id']
        context = {
            'poll':Poll.objects.get(id=poll_id)
        }
    return render(request, 'Content/poll_begin.html', context)

def polls(request):
    context = views_cases.polls_view_data_preparation(request)
    return render(request, "Content/polls.html", context)