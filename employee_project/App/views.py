from django.shortcuts import render,redirect
from .forms import *
from .models import *


def employeeadd(request):

    context = {

        'employee_form' : employees_form()
    }

    if request.method == "POST":

        employeeform = employees_form(request.POST)

        if employeeform.is_valid():
            employeeform.save()

    return render(request,'employees.html',context)

def employee_table(request):

    context = {
        
        'employees_table' : employees.objects.all()
    }

    return render(request,'employee_table.html',context)

def delete_employee(request, id):

    select_employee = employees.objects.get(id = id)

    select_employee.delete()

    return redirect('/app/employee/')

def update_employee(request, id):

    select_employee = employees.objects.get(id = id)

    context= {
        'updateemployee' : employees_form(instance=select_employee)
    }

    if request.method == "POST":

        employeeform = employees_form(request.POST , instance=select_employee)

        if employeeform.is_valid():

            employeeform.save()

            return redirect('/app/employee/')

    return render(request,'employees.html',context)   

