from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30)
    emp_code = models.CharField(max_length=3)
    mobile_number = models.CharField(max_length=10)
