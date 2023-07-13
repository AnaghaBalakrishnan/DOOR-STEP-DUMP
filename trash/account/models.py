from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField(null=True)
    email=models.EmailField()
    message=models.CharField(max_length=1000)
    
