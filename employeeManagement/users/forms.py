from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=myuser
        fields = ('Username', 'Name', 'Email', 'Password', 'Age','Designation','Role','EmployeeNo')
        labels = {'Role':'Role admin/HR/Employee'}
        # or fields = '__all__'
        widgets = {
            'Username': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'Name': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'Email': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'Password': forms.PasswordInput(attrs={'class':'form-control bg-warning'}),
            'Age': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'Designation' : forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'Role' : forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'EmployeeNo' : forms.TextInput(attrs={'class':'form-control bg-warning'}),
            }

class ProjForm(forms.ModelForm):
    class Meta:
        model=projects
        fields = ('Title', 'Project_ID', 'Deadline', 'No_of_Members')
        labels = {'Deadline': 'Deadline (mm/dd/yyyy) '}
        # or fields = '__all__'
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'Project_ID': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'Deadline': forms.DateInput(attrs={'class': 'form-control bg-warning'}),
            'No_of_Members': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            }

class UpdateForm(forms.Form):
    Name = forms.CharField(label='Updated Name', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control bg-warning'}))
    Email = forms.EmailField(label='Updated Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control bg-warning'}))
    Age = forms.CharField(label='Updated Age', max_length=2, widget=forms.TextInput(attrs={'class': 'form-control bg-warning'}))

class ADUpdateForm(forms.Form):
    Name = forms.CharField(label='Updated Name', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control bg-warning'}))
    Email = forms.EmailField(label='Updated Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control bg-warning'}))
    Age = forms.CharField(label='Updated Age', max_length=2, widget=forms.TextInput(attrs={'class': 'form-control bg-warning'}))
    Designation = forms.CharField(label='Updated Designation', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control bg-warning'}))
    Role = forms.CharField(label='Updated Role', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control bg-warning'}))
    EmployeeNo = forms.CharField(label='Updated EmployeeNo', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control bg-warning'}))
    
class ApprForm(forms.ModelForm):
    class Meta:
        model=appraisal
        exclude = ('Username', 'Name', 'Email', 'Password', 'Age','Designation','Role')
        fields = ('appr_no', 'appr_text', 'appr_pts', 'date_of_appr', 'EmployeeNo', 'magr_id')
        labels = {'appr_no':'Appraisal No', 'appr_text':'Notes', 'appr_pts':'Points (/10)', 'date_of_appr':'Date (mm/dd/yyyy) ', 'EmployeeNo':'Employee ID','magr_id':'ID of Appraiser'}
        widgets = {
            'appr_no': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'appr_text': forms.Textarea(attrs={'class':'form-control bg-warning'}),
            'appr_pts': forms.TextInput(attrs={'class': 'form-control bg-warning'}),
            'date_of_appr': forms.DateInput(attrs={'class': 'form-control bg-warning'}),
            'EmployeeNo': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'magr_id': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            }

class RemkForm(forms.ModelForm):
    class Meta:
        model=remarks
        exclude = ('Username', 'Name', 'Email', 'Password', 'Age','Designation','Role')
        fields = ('remk_no', 'remk_text', 'date_of_remk', 'magr_id', 'EmployeeNo')
        labels = {'remk_no':'Remark No', 'remk_text':'Notes', 'date_of_remk':'Date (mm/dd/yyyy) ', 'EmployeeNo':'Employee ID','magr_id':'Manager ID'}
        widgets = {
            'remk_no': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'remk_text': forms.Textarea(attrs={'class':'form-control bg-warning'}),
            'date_of_remk': forms.DateInput(attrs={'class': 'form-control bg-warning'}),
            'EmployeeNo': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            'magr_id': forms.TextInput(attrs={'class':'form-control bg-warning'}),
            }
