from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class meta:
        model = Employee
        fields = "__all__"