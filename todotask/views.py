from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login as auth_login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import views  as auth_views
# Create your views here.

@login_required(login_url=auth_views.LoginView.as_view(template_name='todotask/home.html'))
def home(request):
    return render(request,'todotask/home.html')


def login(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password1)
        if user is not None:
            # the password verified for the user
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
    
        
        if (len(password1)<6 or len(password2)>30):
            return render(request, 'todotask/register.html' , {'pass_error' : 'Password should be between 6 and 30 characters' })
        
        elif password1 != password2:
             return render(request, 'todotask/register.html' , {'pass_error' : 'Passwords do not match! Please try again.' })
        else:
            my_user = User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect('login')
            
        
    return render(request, 'todotask/register.html')