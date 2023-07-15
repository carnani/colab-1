from academy.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude= ['date_joined', 'password', 
            'is_staff', 'groups']