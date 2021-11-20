from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *
from django import forms
from django.db import models

# Create your views here.

def index(request):
    return HttpResponse("Default Page - Users App")

def signup_user(request):
    # if form was submitted
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User Created")
    else:
        form = UserForm
    
    return render(request, 'SignUp.html', {'form':form})

def disp_users(request):
    
    users=[]
    qs = myuser.objects.all()
    for i in qs:
        users.append(i)
    
    return render(request, 'DispUsers.html', {'users':users})

def login_user(request):
    
    cand_usn = request.POST['UN']
    cand_pwd = request.POST['PW']
    user = authenticate(request, username = cand_usn, password = cand_pwd)
    if user is not None:
        login(request, user)
        return redirect('/dashboard')
    else:
        return redirect("/")

def logout_user(request):
    logout(request)
    return redirect("/")

def new_proj(request):
    # if form was submitted
    if request.method == "POST":
        form = ProjForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Project Created")
    else:
        form = ProjForm
    
    return render(request, 'NewProj.html', {'form':form})

def disp_proj(request):
    
    projs=[]
    qs = projects.objects.all()
    for i in qs:
        projs.append(i)
    
    return render(request, 'DispProj.html', {'projs':projs})


# different dashboards for each type of user
# dash shows the two func each user has
