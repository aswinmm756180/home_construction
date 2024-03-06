from django.shortcuts import render,redirect

# Create your views here.



def admin_signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("viewMerchants")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("admin_signin")

    return render(request,"admin/admin_signin.html")

def admin_signout(request):
    logout(request)
    return redirect("admin_signin")




def viewMerchants(request):
    merchants = MerchantProfile.objects.all().order_by("-id")
    # total_turfs = TurfList.objects.all().count()
    # total_managers = ManagerProfile.objects.all().count()
    # total_bookings = Booking.objects.all().count()
    return render(request,"admin/view-merchants.html",{"merchants":merchants,})