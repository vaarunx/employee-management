from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *
from django import forms
from django.db import models
import sqlite3

# Create your views here.

def index(request):
    return render(request,'home.html')

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

def update_user(request):
    # if form was submitted
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            #sql stuff
            #usn = request.user.username
            usn = 'jyang'
            name = request.POST['Name']
            email = request.POST['Email']
            age = request.POST['Age']
            conn = sqlite3.connect("db.sqlite3")
            curr = conn.cursor()
            conn.execute("UPDATE users_myuser SET Name=?, Email=?, Age=? WHERE Username=?", (name,email,age,usn))
            conn.commit()
            conn.close()
            return HttpResponse("User Updated")
    else:
        form = UpdateForm
    
    return render(request, 'UpdateUsers.html', {'form':form})
    
# different dashboards for each type of user
# dash shows the two func each user has

def new_appr(request):
    # if form was submitted
    if request.method == "POST":
        form = ApprForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Appraisal Recorded")
    else:
        form = ApprForm
    
    return render(request, 'NewAppr.html', {'form':form})

def disp_appr(request):
    
    apprs=[]
    qs = appraisal.objects.all()
    for i in qs:
        apprs.append(i)
    
    return render(request, 'DispAppr.html', {'apprs':apprs})

def new_remk(request):
    # if form was submitted
    if request.method == "POST":
        form = RemkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Remark Added")
    else:
        form = RemkForm
    
    return render(request, 'NewRemk.html', {'form':form})

def disp_remk(request):
    
    remks=[]
    qs = remarks.objects.all()
    for i in qs:
        remks.append(i)
    
    return render(request, 'DispRemk.html', {'remks':remks})
