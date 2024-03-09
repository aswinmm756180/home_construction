from django.forms import ModelForm
from django.forms import TextInput,Textarea,NumberInput,DateInput
from .models import MerchantProfile



class MerchantProfileForm(ModelForm):
    class Meta:
        model = MerchantProfile
        fields = ["Address","Company_Name","Phone_Number","Designation"]

        widgets = {
            'Phone_Number': NumberInput(attrs={"class":"form-control","placeholder":"Enter Phone number"}),
            'Designation': TextInput(attrs={"class":"form-control","placeholder":"Enter  Your Designation"}),
            'Address': Textarea(attrs={"class":"form-control","placeholder":"Enter  Address"}),
            'Company_Name': Textarea(attrs={"class":"form-control","placeholder":"Enter  Your Compant Name"}),
        }
        






from django import forms
from .models import ProductList


class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = ProductList  
        fields = '__all__'