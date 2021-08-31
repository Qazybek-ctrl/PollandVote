from django.urls import path
from . import views 

urlpatterns = [
    path('', views.logining_views),
    path('register', views.registration_views)
]