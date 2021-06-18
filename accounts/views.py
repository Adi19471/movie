from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

from .forms import *
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisrationForm(request.POST or None)
        if form.is_valid():
            user =form.save()
            # get the password 
            raw_password = form.cleaned_data.get('password1')
            
            #login the user
            user = authenticate(username=user.username,password=raw_password)
            #login the user

            login(request,user)
            return redirect("home")
    else:
        form = RegisrationForm()

    return render(request,'accounts/register.html',{'form':form})

# login user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
 # check the credintial 
        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("home")
            else:
                return render(request,'accounts/login.html',{'error:','your account has been disbiled'})
        else:
            return render(request,'accounts/login.html',{'error:,' "invalid user name or password.try again"})
        
    return render(request,'accounts/login.html')


def logout_user(request):
    logout(request)
    print("logout succeess")
    return redirect('login')