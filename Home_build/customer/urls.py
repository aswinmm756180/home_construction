from django.urls import path
from .import views
from .views import book_product

urlpatterns=[
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('service',views.service,name="service"),
    path('about',views.about,name="about"),
    path('register',views.register,name="register"),
    path('user_login',views.user_login,name="user_login"),
    path('signout',views.signout,name="signout"),
    path('viewpage/',views.viewpage,name="viewpage"),
    path('category/<str:loc_code>/',views.location_view,name='location_view'),
    path('view_detail/<int:Product_ID>/',views.view_detail,name="view_detail"),
    path('booking/', views.booking_details, name='booking_details'),
    path('book/<int:product_id>/', book_product, name='book_product'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]