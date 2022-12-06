from django.db import models

# Create your models here.
class authentication(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=30)