from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
# Create your views here.


def update_profile(request):
    return render(request, 'users/update_profile.html')

def login_view(request):
    logout(request)
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user:
            login(request, user)
            return redirect('reftable')
        else:
            return render(request,'users/login.html', {'error':'Invalid username or password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    return render(request, 'users/register.html')

@login_required
def home(request):
    return render(request, 'users/home.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def settings(request):
    return render(request, 'users/settings.html')

@login_required
def notifications(request):
    return render(request, 'users/notifications.html')
