from django.shortcuts import render
from .forms import *



def home(request):
    return render(request,'home.html')

def registration(request):
    form = Registration()
    if request.method=='POST':
        data = Registration(request.POST)
        if data.is_valid():
            name=data.cleaned_data['name']
            email=data.cleaned_data['email']
            city=data.cleaned_data['city']
            password=data.cleaned_data['password']
            

            data=render(request,'registration.html')
            data.set_cookie('name',name,max_age=5*24*60*60,httponly=True,secure=True)  #max_age used to set maximum time for cookies data
            data.set_cookie('email',email)   #httponly used to only open it with https
            data.set_cookie('city',city)
            data.set_cookie('password',password)
            return data
    
           
    return render(request,'registration.html',{'form':form})


def login(request):
    form = Login()
    if request.method=="POST":
        data = Login(request.POST)
        if data.is_valid():
            Name= data.cleaned_data['name']
            Email = data.cleaned_data['email']
            Password = data.cleaned_data['password']
            # print(email,password)
          
            nm=request.COOKIES['name']
            em=request.COOKIES['email']
            pas=request.COOKIES['password']
            data = {
                        'name':nm,
                        'email':em,
                        'password':pas
                    }
                    
        return render(request,'get.html',data)
    return render(request,'login.html',{'form':form})