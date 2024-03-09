from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class MerchantProfile(models.Model):
    Phone_Number=models.IntegerField()
    Address=models.CharField(max_length=250)
    Company_Name=models.CharField(max_length=250)
    Designation=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    


Area_choices = (
    ('con', 'con'),
    ('electricals', 'electricals'),
    ('plumbing', 'plumbing'),
    ('interior', 'interior'),
    ('paint', 'paint'),
    ('courtyard', 'courtyard'),
)


class ProductList(models.Model):
    Product_ID=models.AutoField(primary_key=True)
    Product_name=models.CharField(max_length=200)
    Product_price=models.CharField(max_length=200)
    Product_caption=models.CharField(max_length=200)
    Product_image=models.ImageField(null=True ,blank=True,upload_to="product_img")
    Product_area=models.CharField(max_length=200,choices=Area_choices,default='con')


