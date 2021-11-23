from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django import forms
from django.db import models
import sqlite3

# Create your views here.
def get_role(usn):
    qs = myuser.objects.all().filter(Username = usn)
    return qs[0].Role

@csrf_exempt    
def index(request):
    return render(request,'home.html')

@csrf_exempt
def signup_user(request):
    # if form was submitted
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['Username'], email=request.POST['Email'], password=request.POST['Password'])
            user.first_name = request.POST['Name']
            user.save()
            form.save()
            return redirect("/")
    else:
        form = UserForm
    
    return render(request, 'SignUp.html', {'form':form})

@csrf_exempt
def disp_users(request):
    
    users=[]
    qs = myuser.objects.all()
    for i in qs:
        if i.Username!="":
            users.append(i)
    
    return render(request, 'DispUsers.html', {'users':users})

@csrf_exempt
def login_user(request):
    
    cand_usn = request.POST['UN']
    cand_pwd = request.POST['PW']
    user = authenticate(request, username = cand_usn, password = cand_pwd)
    if user is not None:
        login(request, user)
        #retreive role and redirect
        usr_role = get_role(request.user.username)
        if(usr_role=="admin"):
            return redirect("/admindash")
        elif(usr_role=="HR"):
            return redirect("/hrdash")
        elif(usr_role=="Employee"):
            return redirect("/empdash")
        else:
            return HttpResponse('Invalid Role')
    else:
        return redirect("/")

@csrf_exempt
def admin_dash(request):
    return render(request,'AdminDash.html')

@csrf_exempt
def hr_dash(request):
    return render(request,'HRDash.html')

@csrf_exempt
def emp_dash(request):
    return render(request,'EmpDash.html')

@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect("/")

@csrf_exempt
def new_proj(request):
    # if form was submitted
    if request.method == "POST":
        form = ProjForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/disproj")
    else:
        form = ProjForm
    
    return render(request, 'NewProj.html', {'form':form})

@csrf_exempt
def disp_proj(request):
    
    projs=[]
    qs = projects.objects.all()
    for i in qs:
        projs.append(i)
    
    return render(request, 'DispProj.html', {'projs':projs})

@csrf_exempt
def update_user(request):
    # if form was submitted
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            #sql stuff
            usn = request.user.username
            name = request.POST['Name']
            email = request.POST['Email']
            age = request.POST['Age']
            conn = sqlite3.connect("db.sqlite3")
            curr = conn.cursor()
            conn.execute("UPDATE users_myuser SET Name=?, Email=?, Age=? WHERE Username=?", (name,email,age,usn))
            conn.commit()
            conn.close()
            return redirect("/display")
    else:
        form = UpdateForm
    
    return render(request, 'UpdateUsers.html', {'form':form})

@csrf_exempt
def admin_update(request):
    # if form was submitted
    if request.method == "POST":
        form = ADUpdateForm(request.POST)
        if form.is_valid():
            #sql stuff
            usn = request.user.username
            name = request.POST['Name']
            email = request.POST['Email']
            age = request.POST['Age']
            desig = request.POST['Designation']
            role = request.POST['Role']
            empno = request.POST['EmployeeNo']

            conn = sqlite3.connect("db.sqlite3")
            curr = conn.cursor()
            conn.execute("UPDATE users_myuser SET Name=?, Email=?, Age=?, Designation=?, Role=?, EmployeeNo=? WHERE Username=?", (name,email,age,desig,role,empno,usn))
            conn.commit()
            conn.close()
            return redirect("/display")
    else:
        form = ADUpdateForm
    
    return render(request, 'AdminUpdate.html', {'form':form})
    
@csrf_exempt
def new_appr(request):
    # if form was submitted
    if request.method == "POST":
        form = ApprForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dispappr")
    else:
        form = ApprForm
    
    return render(request, 'NewAppr.html', {'form':form})

@csrf_exempt
def disp_appr(request):
    
    apprs=[]
    qs = appraisal.objects.all()
    for i in qs:
        apprs.append(i)
    
    return render(request, 'DispAppr.html', {'apprs':apprs})

@csrf_exempt
def new_remk(request):
    # if form was submitted
    if request.method == "POST":
        form = RemkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dispremk")
    else:
        form = RemkForm
    
    return render(request, 'NewRemk.html', {'form':form})

@csrf_exempt
def disp_remk(request):
    
    remks=[]
    qs = remarks.objects.all()
    for i in qs:
        remks.append(i)
    
    return render(request, 'DispRemk.html', {'remks':remks})

@csrf_exempt
def del_emp_form(request):
    return render(request,'DelEmp.html')

@csrf_exempt
def del_proj_form(request):
    return render(request,'DelProj.html')

@csrf_exempt
def del_proj(request):
    
    projno = request.POST['projno']
    conn = sqlite3.connect("db.sqlite3")
    curr = conn.cursor()
    conn.execute("DELETE FROM users_projects WHERE Project_ID="+projno)
    conn.commit()
    conn.close()
    return redirect("/disproj")

@csrf_exempt
def del_emp(request):
    
    empno = request.POST['empno']
    print(empno)
    conn = sqlite3.connect("db.sqlite3")
    curr = conn.cursor()
    conn.execute("DELETE FROM users_myuser WHERE EmployeeNo="+empno)
    conn.commit()
    conn.close()
    return redirect("/display")
