from django.urls import path
from .views import *

urlpatterns =[
    path('employeeadd/',employeeadd),
    path('employee/',employee_table),
    path('employee/delete/<int:id>/',delete_employee, name='employeedelete'),
    path('employee/update/<int:id>/',update_employee, name='employeeupdate'),
    
]
