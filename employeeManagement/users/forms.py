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
    
class ApprForm(forms.ModelForm):
    class Meta:
        model=appraisal
        exclude = ('Username', 'Name', 'Email', 'Password', 'Age','Designation','Role')
        fields = ('appr_no', 'appr_text', 'appr_pts', 'date_of_appr', 'EmployeeNo', 'magr_id')
        labels = {'appr_no':'Appraisal No', 'appr_text':'Notes', 'appr_pts':'Points (/10)', 'date_of_appr':'Date (mm/dd/yyyy) ', 'EmployeeNo':'Employee ID','magr_id':'ID of Appraiser'}
        widgets = {
            'appr_no': forms.TextInput(attrs={'class':'form-control'}),
            'appr_text': forms.Textarea(attrs={'class':'form-control'}),
            'appr_pts': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_appr': forms.DateInput(attrs={'class': 'form-control'}),
            'EmployeeNo': forms.TextInput(attrs={'class':'form-control'}),
            'magr_id': forms.TextInput(attrs={'class':'form-control'}),
            }

class RemkForm(forms.ModelForm):
    class Meta:
        model=remarks
        exclude = ('Username', 'Name', 'Email', 'Password', 'Age','Designation','Role')
        fields = ('remk_no', 'remk_text', 'date_of_remk', 'magr_id', 'EmployeeNo')
        labels = {'remk_no':'Remark No', 'remk_text':'Notes', 'date_of_remk':'Date (mm/dd/yyyy) ', 'EmployeeNo':'Employee ID','magr_id':'Manager ID'}
        widgets = {
            'remk_no': forms.TextInput(attrs={'class':'form-control'}),
            'remk_text': forms.Textarea(attrs={'class':'form-control'}),
            'date_of_remk': forms.DateInput(attrs={'class': 'form-control'}),
            'EmployeeNo': forms.TextInput(attrs={'class':'form-control'}),
            'magr_id': forms.TextInput(attrs={'class':'form-control'}),
            }
