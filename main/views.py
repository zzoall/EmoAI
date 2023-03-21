from django.shortcuts import render
import datetime
from datetime import timedelta

def index(request):
    return render(
        request,
        'index.html'
    )

def demo(request):
    return render(request, 'demo.html')


def contact(request):
    return render(
        request,'contact.html')

def about(request):
    return render(
        request,'about.html')

def service(request):
    return render(request, 'service.html')

def profile(request):
    return render(request, 'profile.html')

def userinfo(request):
    return render(request, 'userinfo.html')

def login(request):
    return render(request, 'login.html')

def password(request):
    return render(request, 'password.html')

def register(request):
    return render(request, 'register.html')
