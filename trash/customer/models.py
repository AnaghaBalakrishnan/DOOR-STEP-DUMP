from django.db import models
from .models import *
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    category=models.CharField(max_length=100)
    customer_fee=models.IntegerField()
    description=models.CharField(max_length=300)
    image=models.FileField(upload_to='profile_images') 


class Booking(models.Model):
    cname=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=1000)
    ph=models.IntegerField(null=True)
    type=models.ForeignKey(Categories,on_delete=models.CASCADE)
    number_of_bags=models.IntegerField(null=True) 
    date=models.DateField(null=True)
   
    
    
    

      
