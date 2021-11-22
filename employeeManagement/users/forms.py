from django import forms
from .models import *

class UserForm(forms.ModelForm):
    
    class Meta:
        model=myuser
        fields = ('Username', 'Name', 'Email', 'Password', 'Age','Designation','Role','EmployeeNo')
        # or fields = '__all__'
        widgets = {
            'Username': forms.TextInput(attrs={'class':'form-control'}),
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.TextInput(attrs={'class':'form-control'}),
            'Password': forms.PasswordInput(attrs={'class':'form-control'}),
            'Age': forms.TextInput(attrs={'class':'form-control'}),
            'Designation' : forms.TextInput(attrs={'class':'form-control'}),
            'Role' : forms.TextInput(attrs={'class':'form-control'}),
            'EmployeeNo' : forms.TextInput(attrs={'class':'form-control'}),
            }

class ProjForm(forms.ModelForm):
    
    class Meta:
        model=projects
        fields = ('Title', 'Project_ID', 'Deadline', 'No_of_Members')
        labels = {'Deadline': 'Deadline (mm/dd/yyyy) '}
        # or fields = '__all__'
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'Project_ID': forms.TextInput(attrs={'class':'form-control'}),
            'Deadline': forms.DateInput(attrs={'class': 'form-control'}),
            'No_of_Members': forms.TextInput(attrs={'class':'form-control'}),
            }

class UpdateForm(forms.Form):
    
    Name = forms.CharField(label='Updated Name', max_length=25)
    Email = forms.EmailField(label='Updated Email', max_length=100)
    Age = forms.CharField(label='Updated Age', max_length=2)
