from django.urls import path
from .import views



urlpatterns=[
    path('admin_signin', views.admin_signin, name='admin_signin'),
    path('viewMerchants',views.viewMerchants,name="viewMerchants"),
     path('approveMerchant/<int:m_id>/',views.approveMerchant,name="approveMerchant"),
    path('removeMerchant/<int:m_id>/',views.removeMerchant,name="removeMerchant"),
    path('admin_signout',views.admin_signout,name='admin_signout'),
]