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
    general = Poll.objects.filter(category="general")
    context['general'] = len(general)

    lifestyle = Poll.objects.filter(category="lifestyle")
    context['lifestyle'] = len(lifestyle)

    travel = Poll.objects.filter(category="travel")
    context['travel'] = len(travel)

    design = Poll.objects.filter(category="design")
    context['design'] = len(design)

    creative = Poll.objects.filter(category="creative")
    context['creative'] = len(creative)

    education = Poll.objects.filter(category="education")
    context['education'] = len(education)
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
        'poll':Poll.objects.get(id=poll_id),
        'active':request.user.is_authenticated
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

def poll_creation(request):
    user = request.user
    title = request.POST['title']
    desc = request.POST['description']
    option1 = request.POST['option1']
    option2 = request.POST['option2']
    option3 = request.POST['option3']
    category = request.POST['category']
    poll = Poll()
    poll.title = title
    poll.description = desc
    poll.category = category
    poll.option1 = option1
    poll.option2 = option2
    poll.option3 = option3
    poll.owner_id = user
    poll.save()
    vote = Voted(user_id=user.id, poll_id=poll.id)
    vote.save()
    return redirect("polls")
