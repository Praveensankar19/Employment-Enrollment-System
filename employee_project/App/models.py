from django.db import models

# Create your models here.

class employees(models.Model):

    fullname = models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200,null=True)
    mobile_no = models.BigIntegerField()
    role = models.CharField(max_length=200, null=True)
    location=models.CharField(max_length=200,null=True)

    def __str__(self):

        return self.fullname
    
