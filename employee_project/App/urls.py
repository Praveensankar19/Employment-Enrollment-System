from django.urls import path
from .views import *


urlpatterns =[
    path('home/', employee_table),
    path('employeeadd/', employeeadd),
    path('employee/delete/<int:id>/', delete_employee, name='employeedelete'),
    path('employee/update/<int:id>/', update_employee, name='employeeupdate'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]

