from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def registration(request):
    if request.method=='POST':
        name=request.POST['first']
        email=request.POST['email']
        number=request.POST['mobile']
        gender=request.POST['gender']
        college=request.POST['college']
        password=request.POST['password']
        confirm_password=request.POST['repassword']
        if password==confirm_password:
            user=participant(name=name,email=email,password=password,participant_ph=number,gender=gender,college=college)
            user.save()
            return redirect('login')
            # print("Registration Successfull")
        else:
            messages.info(request,"password not correct")
            return redirect('registration')
        # print("password not correct")
    return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']
            user=participant.objects.get(email=email,password=password)
            if user is not None:
              return redirect('profile')
            else:
              messages.info(request,"Invalid")
              return redirect('login')
    return render(request,'login.html')

def logout(request):
    return redirect('/')

def profile(request):
    return render(request,'profile.html')

def myprofile(request):
    return render(request,"myprofile.html")

