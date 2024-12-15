from django.forms import ModelForm
from .models import *

class employees_form(ModelForm):

    class Meta:

        model = employees
        fields = '__all__'
