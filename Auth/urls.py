from django.urls import path
from . import views 

urlpatterns = [
    path('', views.logining_view, name="auth"),
    path('register', views.registration_view, name="reg")
]