from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Content/home.html')

def polls(request):
    return render(request, "Content/polls.html")