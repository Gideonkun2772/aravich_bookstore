from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from .form import registerform,loginform
from django.contrib.auth.models import User
from django.contrib import messages
#create your views here

form=registerform()
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user=User.objects.create_user(username=username,password=password1,email=email)
            user.save();
            print('user created')
            return redirect('/')
        else:
            print('password not matching')
            
    else:
        return render(request,'accounts/register.html',{'form':form})
    
    
    
def loginview(request):
    if request.method=='GET':
        form=loginform()
        return render(request,'accounts/login.html',{'form':form})
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       # message.success(request,'')
    else:        
         return render(request,'accounts/login.html',{'form':form(request.POST)})

def logout(request):
    auth.logout(request)
    return redirect('/')