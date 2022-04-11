"""Power URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from mainapp import views as main_view
from adminapp import views as admin_view
from userapp import views as user_view
from billingapp import views as billing_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # main
    
    path('',main_view.index,name='index'),
    path('about',main_view.about,name='about'),
    path('contact',main_view.contact,name='contact'),
   
    
    
    
    # admin
    
    path('admin-login',admin_view.adminlogin,name='admin_login'), 
    path('adminhome',admin_view.adminhome,name='adminhome'),
    path('viewconnection',admin_view.viewconnection,name='viewconnection'),
    path('newconnection_update/<int:id>',admin_view.newconnection_update,name='newconnection_update'),
    path('newconnection_update_reject/<int:id>/',admin_view.newconnection_update_reject ,name='newconnection_update_reject'),
    path('viewusercomplaint',admin_view.viewusercomplaint,name='viewusercomplaint'),
    path('deletecomplaint/<int:id>/',admin_view.deletecomplaint ,name='deletecomplaint'),
    path('viewfeedback',admin_view.viewfeedback,name='viewfeedback'),
    path('deleteuserfeedback/<int:id>/',admin_view.deleteuserfeedback ,name='deleteuserfeedback'),
    path('view-biller',admin_view.view_biller,name='view-biller'),
     path('removebiller/<int:id>/',admin_view.removebiller ,name='removebiller'),
    path('add-biller',admin_view.add_biller,name='add-biller'),
    path('view-billing',admin_view.view_billing,name='view-billing'),
    
    # user

    path('user',user_view.userlogin,name='user'),
    path('userlogin',user_view.userlogin,name='userlogin'),
    path('userhome',user_view.userhome,name='userhome'),
    path('userregister',user_view.userregister,name='userregister'),
    path('newconnection',user_view.newconnection,name='newconnection'),
    path('raisecomplaint',user_view.raisecomplaint,name='raisecomplaint'),
    path('servicefeedback',user_view.servicefeedback,name='servicefeedback'),
    path('user-view-bill',user_view.user_view_bill,name='view_bill'),
    path('user-payment-method-debit',user_view.user_debit,name='user_debit'),
    path('user-payment-method-credit',user_view.user_credit,name='user_credit'),
    path('user-payment-method-upi',user_view.user_upi,name='user_upi'),
    
    

    # biller

    path('biller-login',billing_view.billerlogin,name='biller_login'),
    path('billinghome',billing_view.billinghome,name='billinghome'),
    path('billgeneration',billing_view.billgeneration,name='billgeneration'),
    # path('billgeneration-view_bill_details/<int:id>/',billing_view.view_bill_details,name='billgeneration-view_bill_details'),
    path('billing-generation-enter-unit/<int:id>',billing_view.billingunit,name='billing-generation-enter-unit'), 


]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
