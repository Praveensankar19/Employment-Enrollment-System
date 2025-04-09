from django.db import models

class employees(models.Model):

    DEPARTMENT_CHOICES = [
        ('Software Development', 'Software Development'),
        ('Testing', 'Testing'),
        ('Sales', 'Sales'),
        ('Customer Support', 'Customer Support'),
        ('Technical Support', 'Technical Support'),
        ('Manager', 'Manager'),
        ('HR', 'HR'),
    ]

    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
 

    fullname = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    mobile_no = models.CharField(max_length=10,unique=True)
    destination = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, choices=DEPARTMENT_CHOICES, null=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    experience = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True) 
    age = models.PositiveIntegerField(null=True, blank=True)
    dob = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.fullname
    
