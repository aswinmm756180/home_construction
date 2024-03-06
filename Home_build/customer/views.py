from django.shortcuts import render,redirect
from .forms import UserAddForm
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    return render(request,"service.html")



def viewpage(request):
    return render(request,"user/viewpage.html")


def register(request):
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='users')
            user.groups.add(group)
            login(request, user)  # Correct usage of login function
            messages.success(request, "New User Created")
            return redirect('user_login')
        else:
            messages.error(request, "Form validation failed. Please try a different password.")
            print("Form errors:", form.errors)
    else:
        form = UserAddForm()
    return render(request,"user/register.html",{"form":form})

def user_login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("viewpage")
        else:
            
            messages.info(request,"Username or Password Incorrect")
            return redirect("user_login")
    return render(request,"user/login.html")

def signout(request):
    
    logout(request)
    return redirect('user_login')