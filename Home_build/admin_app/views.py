from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from merchant.models import MerchantProfile
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

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
    merchant = MerchantProfile.objects.all().order_by("-id")
    # total_turfs = TurfList.objects.all().count()
    # total_managers = ManagerProfile.objects.all().count()
    # total_bookings = Booking.objects.all().count()
    return render(request,"admin/view-merchants.html",{"merchants":merchant})






def approveMerchant(request,m_id):
    merchant = User.objects.get(id = m_id)
    merchant.is_active = True
    merchant.save()
    messages.success(request,"Approved as Merchant")
    return redirect("viewMerchants")


from django.shortcuts import get_object_or_404
from django.contrib import messages




def removeMerchant(request, m_id):
    try:
        merchant = get_object_or_404(User, id=m_id)

        # Access related profile using the default related name (user_set)
        merchant_profile_set = merchant.merchantprofile_set.all()

        # Assuming there is only one related profile, you can delete it
        if merchant_profile_set:
            merchant_profile_set[0].delete()

        # Delete the User instance
        merchant.delete()

        messages.success(request, "Removed Merchantr")
    except Exception as e:
        # Print the exception for debugging
        print(f"Error removing merchant: {str(e)}")
        messages.error(request, "Error removing merchant")

    return redirect("viewMerchants")