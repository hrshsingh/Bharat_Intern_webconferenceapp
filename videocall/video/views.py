from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from video.forms import RegisterUser
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return render(request,'login.html',{'success':"registered"})
        else:
            error_meessage=form.errors.as_text()
            return render(request,'register.html',{'error':"there is a error"})
    
    return render(request,'register.html')


def login_us(request):
    if request.method == 'POST' :
        email=request.POST.get('email')
        password=request.POST.get('password')
        print (email)
        print(password)
        user = authenticate(request,username=email,password=password)
        print (user)
        if user is not None:
            login(request,user)
            return redirect('/home/')
            #return redirect('home')

            # User is authenticated
        else:
            return render(request,'login.html',{'error':"not verified occured"})
    
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html',{'name': request.user.first_name})

@login_required
def videocall(request):
    return render(request, 'videocall.html',{'name': request.user.first_name})

@login_required
def logout_vu(request):
    logout(request)
    return redirect("/login")

@login_required
def join_room(request):
    if request.method=='POST':
        t=request.POST.get('link')
        return redirect("/meeting?roomID="+t)
    return render(request, 'joinroom.html',{'name': request.user.first_name})