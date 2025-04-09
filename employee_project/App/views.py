from django.shortcuts import render,redirect 
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/app/home/')  # redirect after successful login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # name of the login path in urls.py

    return render(request, 'login.html')


def employeeadd(request):
    if request.method == "POST":
        employeeform = employees_form(request.POST)
        if employeeform.is_valid():
            employeeform.save()
            return redirect('/app/employee/')  # Redirect to refresh and show updated list
    else:
        employeeform = employees_form()

    context = {
        'employee_form': employeeform,
        'employees_table': employees.objects.all()     # fetches the data
    }

    return render(request, 'employee_form.html', context)


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
    select_employee = employees.objects.get(id=id)

    if request.method == "POST":
        employeeform = employees_form(request.POST, instance=select_employee)
        if employeeform.is_valid():
            employeeform.save()
            return redirect('/app/employee/')
    else:
        employeeform = employees_form(instance=select_employee)

    context = {
        'employee_form': employeeform,  # use same key as in add view
        'employees_table': employees.objects.all()
    }

    return render(request, 'employee_form.html', context)


