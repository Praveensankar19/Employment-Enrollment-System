from django import forms
from django.forms import ModelForm
from .models import employees
import re

class employees_form(ModelForm):
    class Meta:
        model = employees
        fields = '__all__'

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }


 # clean_fieldname()  ----------> Django ModelForm allows you to add custom validations
 # cleaned_data ------->  dictionary that Django automatically creates after you call form.is_valid()
 # re --------> regular expression for validate the format 

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if location and len(location) < 3:
            raise forms.ValidationError("Location must be at least 3 characters long.")
        return location

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is not None and salary < 10000:
            raise forms.ValidationError("Salary must be at least 10,000.")
        return salary

    def clean_experience(self):
        experience = self.cleaned_data.get('experience')
        if experience is not None and experience < 0:
            raise forms.ValidationError("Experience cannot be negative.")
        return experience 


