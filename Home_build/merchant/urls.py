from django.urls import path
from .import views




urlpatterns=[
    path('',views.product_detail,name="product_detail"),
    path("merchantsignup",views.merchantsignup,name="merchantsignup"),
    path("merchantsignin",views.merchantsignin,name="merchantsignin"),
    path("merchantsignout",views.merchantsignout,name="merchantsignout"),
    path("add_product/",views.add_product,name="add_product"),
    path('deleteproduct/<int:pk>',views.deleteproduct,name="deleteproduct"),
    path('edit_product/<int:tid>',views.edit_product,name='edit_product'),
]