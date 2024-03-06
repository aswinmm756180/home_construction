from django.shortcuts import render

# Create your views here.
















from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MerchantProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def Merchantsignup(request):
    form=UserAddForm()
    merchant_form=MerchantProfileForm()
    if request.method=="POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Already Exists")
                return redirect('merchantsignup')
            if User.objects.filter(email=email).exists():
                messages.info(request,"This Emailid is Already Taken")
                return redirect('merchantsignup')
            
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
                
            group = Group.objects.get(name='merchant')
            new_user.groups.add(group) 

            merchant_form = MerchantProfileForm(request.POST,request.FILES)
            if merchant_form.is_valid():
                merchant = merchant_form.save()
                merchant.user = new_user
                merchant.save()
                messages.success(request,"Registered as Merchant! Wait for Approval")
                return redirect('merchantsignin')
            else:
                messages.success(request,"Couldn't perform  Signup")
        else:
            messages.error(request,"Error in merchant profile details.")
    return render(request,"merchant\signup.html",{"form":form,"merchant_form":merchant_form})


