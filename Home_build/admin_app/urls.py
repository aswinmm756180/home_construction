from django.urls import path
from .import views



urlpatterns=[
    path('admin_signin', views.admin_signin, name='admin_signin'),
    path('viewMerchants',views.viewMerchants,name="viewMerchants"),
    path('signout',views.admin_signout,name='admin_signout'),
]