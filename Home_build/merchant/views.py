from django.shortcuts import render,redirect
from customer.forms import UserAddForm
from .forms import MerchantProfileForm
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import ProductList
from .forms import ProductDetailsForm
from django.contrib.auth.decorators import login_required
# from datetime import timedelta
# from users_app.models import Booking,Message




# Create your views here.



def product_detail(request):
    products=ProductList.objects.all().order_by("-Product_ID")
    return render(request,"merchant/merchant_index.html",{"all_Product":products})












from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.shortcuts import render, redirect
from customer.forms import UserAddForm
from merchant.forms import MerchantProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def merchantsignup(request):
    form=UserAddForm()
    merchant_form = MerchantProfileForm()
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
                print(form.errors)

        else:
            messages.error(request,"Error in merchant profile details.")
    return render(request,"merchant/signup.html",{"form":form,"merchant_form":merchant_form})




def merchantsignin(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            messages.info(request,'Logged In Successfully')
            login(request, user1)
            group = request.user.groups.all()[0].name
            if(group == "merchant"):
                return redirect('product_detail')
            else:
                messages.info(request,'Username or Password Incorrect')
                return redirect("merchantsignout")
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('merchantsignin')
    return render(request,"merchant/signin.html")




def merchantsignout(request):
    logout(request)
    return redirect('index')


def deleteproduct(request,pk):
    edit=ProductList.objects.get(Product_ID=pk)
    edit.delete()
    messages.info(request,"deleted")
    return redirect("product_detail")


Area_choices = (
    ('construction', 'construction'),
    ('electricals', 'electricals'),
    ('plumbing', 'plumbing'),
    ('interior', 'interior'),
    ('paint', 'paint'),
    ('courtyard', 'courtyard'),
)


def add_product(request):
    if request.method == 'POST':
        form = ProductDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Successfully Added")
            return redirect('product_detail')
    else:
        form = ProductDetailsForm()

    return render(request, "merchant/add_product.html", {'form': form, 'Area_choices': Area_choices})

from django.urls import reverse
from django.shortcuts import render

def edit_product(request,tid):
    edit_product=ProductList.objects.get( Product_ID=tid)
    if request.method == "POST":
        edit_product.Product_name=request.POST["Product_name"]
        # edit_product.Product_address=request.POST["Product_address"]
        edit_product.Product_price=request.POST["Product_price"]
        edit_product.Product_caption=request.POST["Product_caption"]
        if "Product_image" in request.FILES:
            edit_product.Product_image=request.FILES["Product_image"]
        edit_product.save()
        return redirect("product_detail")
    return render(request,"merchant\edit_product.html",{"edit_product":edit_product}) 



