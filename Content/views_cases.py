from .models import Poll, Voted
from django.contrib.auth.models import User


def polls_view_data_preparation(request):
    context = {
        'active':request.user.is_authenticated,
        'polls':Poll.objects.all()
    }
    return context