from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserAddForm
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from merchant.models import ProductList
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



def view_detail(request,Product_ID):
    product=get_object_or_404(ProductList,pk=Product_ID)
    return render(request,"user/view_product.html",{'product':product})



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




# def category(request):
#     return render(request,'user/viewpage.html')





# category selection

Area_choices = (
    ('construction', 'construction'),
    ('electricals', 'electricals'),
    ('plumbing', 'plumbing'),
    ('interior', 'interior'),
    ('paint', 'paint'),
    ('courtyard', 'courtyard'),
)


def location_view(request, loc_code):
    location_products = []
    context = {}  # Initialize context outside the loop

    for code, name in Area_choices:
        if code == loc_code:
            products = ProductList.objects.filter(Product_area=code)
            location_products.append({'location_name': name, 'products': products})
            break

    context['location_products'] = location_products
    return render(request, 'user/location_product.html', context)

from customer.models import Booking

def booking_details(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'user/my_booking.html', {'bookings': bookings})



from django.shortcuts import render, redirect, get_object_or_404
from customer.models import Booking  # Import your Booking model
from merchant.models import ProductList  # Import your ProductList model
from django.contrib.auth.decorators import login_required  # Import login_required decorator

@login_required
def book_product(request, product_id):
    selected_product = get_object_or_404(ProductList, id=product_id)
    if request.method == 'POST':
        game1 = request.POST.get('game')
        date1 = request.POST.get('date')
        quantity1 = request.POST.get('quantity')
        address1 = request.POST.get('address')
        phone_number1 = request.POST.get('phone_number')

        # Create a Booking instance
        booking = Booking(
            user=request.user,
            product=selected_product,
            game=game1,
            date=date1,
            quantity=quantity1,
            address=address1,
            phone_number=phone_number1,
        )
        booking.save()
        return redirect('booking_details')  # Redirect to the booking details page

    return render(request, 'user/view_product.html', {'product': selected_product})





# def book_product(request, product_id):
#     disp=Booking.objects.all()
#     return render(request,'my_booking.html',{'Bookings':disp})





def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('booking_details')