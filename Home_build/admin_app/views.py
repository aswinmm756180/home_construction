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
            # return redirect("viewManagers")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("admin_signin")

    return render(request,"admin/admin_signin.html")

def admin_signout(request):
    logout(request)
    return redirect("admin_signin")