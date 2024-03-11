from django.db import models
from merchant.models import MerchantProfile,ProductList
from django.contrib.auth.models import User
from .models import ProductList


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
    game = models.CharField(max_length=20, choices=game_choices, default='Thiruvananthapuram')
    quantity = models.IntegerField()
    address = models.CharField(max_length=150)
    date = models.DateField()
    phone_number = models.CharField(max_length=15)  # Changed from IntegerField to CharField

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.game}"