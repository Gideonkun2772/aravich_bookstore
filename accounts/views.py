from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .form import register,loginform
#create your views here

form=register
def register(request):
    return render(request,'accounts/register.html',{'form':register})
def loginview(request):
    return render(request,'accounts/login.html',{'login':loginform})