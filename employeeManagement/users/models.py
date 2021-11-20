from django.db import models

# Create your models here.

class myuser(models.Model):
    
    Username = models.CharField(max_length=15)
    Name = models.CharField(max_length=25)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=15)
    Age = models.CharField(max_length=2)
    Designation = models.CharField(max_length=15)
    Role = models.CharField(max_length=15)
    EmployeeNo = models.CharField(max_length=15)
    

class projects(models.Model):
    
    Title = models.CharField(max_length=150)
    Project_ID = models.CharField(max_length=10)
    Deadline = models.DateField()
    No_of_Members = models.CharField(max_length=3)
