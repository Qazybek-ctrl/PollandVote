from django.shortcuts import redirect, render
from .models import Poll, Voted
from django.contrib.auth.models import User


def polls_view_data_preparation(request):
    context = {
        'active':request.user.is_authenticated,
        'polls':Poll.objects.all()
    }
    votes = Voted.objects.filter(user_id=request.user.id)
    voted_polls_id = []
    for vote in votes:
        voted_polls_id.append(vote.poll_id)
    context['votes'] = voted_polls_id
    return context

def user_voting(request):
    answer = request.POST['answer']
    poll_id = request.POST['poll_id']
    poll = Poll.objects.get(id=poll_id) 
    user = User.objects.get(id=request.user.id)
    vote = Voted(user_id = user.id, poll_id = poll.id)
    vote.save()
    if answer == poll.option1:
        poll.votes1 = int(poll.votes1) + 1
    elif answer == poll.option2:
        poll.votes2 = int(poll.votes2) + 1
    elif answer == poll.option3:
        poll.votes3 = int(poll.votes3) + 1
    
    poll.total_votes = int(poll.total_votes) + 1
    poll.save()

    return redirect('success')

def check_user_validity(request):
    poll_id = request.GET['poll_id']
    context = {
        'poll':Poll.objects.get(id=poll_id)
    }
    try:
        vote = Voted.objects.get(
            user_id=request.user.id,
            poll_id=poll_id    
        ) 
    except:
        return render(request, 'Content/poll_begin.html', context)
    else:
        return redirect("error")