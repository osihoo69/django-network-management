from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request, 'network_management/home.html')

def loginuser(request):
    if request.method =='GET':
            return render(request, 'network_management/login.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'network_management/login.html',{'form':AuthenticationForm(), 'error':'Username or Password incorrect'})
        else:
            login(request, user)
            return redirect('home')

def logoutuser(request):
#    if request.method =='POST':
        logout(request)
        return redirect('loginuser')
    
    
    
    

