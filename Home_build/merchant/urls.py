from django.urls import path
from .import views




urlpatterns=[
    path("merchantsignup",views.merchantsignup,name="merchantsignup"),
    path("merchantsignin",views.merchantsignin,name="merchantsignin"),
    path("merchantsignout",views.merchantsignout,name="merchantsignout"),
]