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

class appraisal(myuser):
    #extends myuser
    appr_no = models.CharField(max_length=6)
    appr_text = models.CharField(max_length=300)
    appr_pts = models.CharField(max_length=2)
    date_of_appr = models.DateField()
    magr_id = models.CharField(max_length=15)


    def __str__(self):
        return f'{self.appr_no}'

class remarks(myuser):
    #extends myuser
    remk_no = models.CharField(max_length=6)
    remk_text = models.CharField(max_length=300)
    date_of_remk = models.DateField()
    magr_id = models.CharField(max_length=15)
