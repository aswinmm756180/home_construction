from django.db import models
from merchant.models import MerchantProfile,ProductList
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE, null=True)
    game_choices = [
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Kollam', 'Kollam'),
        ('Alappuzha', 'Alappuzha'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Kottayam', 'Kottayam'),
        ('Idukki', 'Idukki'),
        ('Ernakulam', 'Ernakulam'),
        ('Thrissur', 'Thrissur'),
        ('Palakkad', 'Palakkad'),
        ('Malappuram', 'Malappuram'),
        ('Kozhikode', 'Kozhikode'),
        ('Wayanad', 'Wayanad'),
        ('Kannur', 'Kannur'),
        ('Kasaragod', 'Kasaragod'),
    ]
    game = models.CharField(max_length=20, choices=game_choices, default='Football')
    quantity = models.DateTimeField(null=True)
    address = models.DateTimeField(null=True)
    date = models.DateField(null=True)
    phone_number = models.CharField(max_length=15)