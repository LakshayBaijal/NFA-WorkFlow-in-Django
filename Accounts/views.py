from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pname1=request.POST['password1']
        pname2=request.POST['password2']

        if pname1==pname2:
            if User.objects.filter(username=username).exists():
                return render(request,'register.html',{'error':'Username is already taken'})
            elif User.objects.filter(email=email).exists():
                return render(request,'register.html',{'error':'Email is already taken'})
            else:
                user= User.objects.create_user(username=username,password=pname1,email=email)
                user.save()
                user = auth.authenticate(username=username,password=pname1)
                auth.login(request,user)
                return redirect('/')
        else:
            return render(request,'register.html',{'error':'Password didnt match'})
            # return render(request,'register.html')
    else:
        return render(request,'register.html')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            # return render(request,'index.html')
            return redirect('/')

        else:
            # return render(request,'login.html')
            return redirect('login')
    else:
        return render(request,'login.html')
        
    
def logout(request):
    auth.logout(request)
    return redirect('/')