from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login as auth_login 
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'todotask/home.html')


def login(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password1)
        if user is not None:
            # the password verified for the user
            print("User Logged In")
            auth_login(request,user)
            return redirect('home')
        else:
            # the password was incorrect
            print("Wrong Password or Username")
            return render(request,"todotask/login.html",{'error':'Invalid Credentials!'})
            
    return render(request,'todotask/login.html',{})
    

def register(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')
        my_user = User.objects.create_user(username,email,password1)
        my_user.save()
        return redirect('login')
        
    return render(request, 'todotask/register.html')