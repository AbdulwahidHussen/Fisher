from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login
from .models import *
from .models import Info
from django.contrib.auth.models import User
from .forms import UserInfo, UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def login(request):
    form = UserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request.user)
            info = Info.objects.all().filter(whos=user)
            return render(request, 'user-dashboard.html', {'userinf': info})
        else:
            messages.error(request, 'invalid username or password')

    return render(request, 'registration/register.html', {'form': form, 'signup': False})

def register(request):
    form = UserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['password']
        email = request.POST['email']
        password2 = request.POST.get('password2')
        if password==password2:
            if User.objects.all().filter(email=email).exists():
                messages.error(request, 'email already registered')
            elif User.objects.all().filter(username=username).exists():
                messages.error(request, 'username already registered')

            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    info = Info.objects.all().filter(whos=user)
                    return render(request, 'user-dashboard.html', {'userinf':info})
                else:
                    User.objects.create_user(username,email,password)
                    return redirect('login')
        else:
            messages.error(request, 'passwords dont match')
    return render(request, 'registration/register.html',{'form':form,'signup':'s'})
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'user-dashboard.html', {'userinf': 'info'})