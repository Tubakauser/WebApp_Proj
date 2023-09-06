from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

def welcome(request):
    return render(request,'welcome.html')

def load_form(request):
    form = EmployeeForm
    return render(request,'index.html',{'form': form})

def Add(request):
    form = EmployeeForm(request.POST)
    form = save()
