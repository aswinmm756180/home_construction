from django.urls import path
from .import views




urlpatterns=[
    path("Merchantsignup",views.Merchantsignup,name="Merchantsignup"),
]