from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentails")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        mail=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cnfmpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=mail)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
