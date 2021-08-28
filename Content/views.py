from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Content/index.html')

def blog(request):
    return render(request, "Content/blog.html")