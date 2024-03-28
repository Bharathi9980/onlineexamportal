from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def generalhomepage(request):
    return render(request,'generalhomepage.html')
def projecthomepage(request):
    return render(request,'projecthomepage.html')

def facultyhompage(request):
    return render(request, 'facultyhomepage.html')

def studenthomepage(request):
    return render(request,'studenthomepage.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            if len(username)>=6:
                return redirect('studenthomepage')
            elif len(username)==4:
                return redirect('facultyhomepage')
            elif len(username)==5:
                return redirect('projecthomepage')
            else:
                return redirect('generalhomepage')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup1(request):
 if request.method=="POST":
     username=request.POST['username']
     pass1=request.POST['password']
     pass2=request.POST['password1']
     if pass1==pass2:
             if User.objects.filter(username=username).exists():
                 messages.info(request,'OOPS! Username is already taken')
                 return render(request,'signup.html')
             else:
                 user=User.objects.create_user(username=username,password=pass1)
                 user.save()
                 messages.info(request,'Account created successfully!!')
                 return render(request,'login.html')
     else:
             messages.info(request,'Password do not match')
             return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'generalhomepage.html')