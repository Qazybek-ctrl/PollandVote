from Content import views_cases
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('polls', views.polls, name="polls"),
    path('poll-start', views.start_poll_view, name="poll"),
    path('accepted-vote', views.accepted_poll_view, name="success"),
    path('second-voting-error', views.second_vote_view, name="error"),
    path('third-error', views.third_vote_view, name="error2"),
    path('poll_creation', views.poll_creation_view, name="create")
]