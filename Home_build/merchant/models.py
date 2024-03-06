from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class MerchantProfile(models.Model):
    Phone_Number=models.IntegerField()
    Address=models.CharField(max_length=250)
    Company_Name=models.CharField(max_length=250)
    Designation=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
