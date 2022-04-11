import numbers
from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import AddBillerModel 

from userapp.models import NewconnectionModel, RaisecomplaintsModel, ServicefeedbackModel
import random

from django.core.mail import EmailMultiAlternatives
from Power.settings import DEFAULT_FROM_EMAIL


# Create your views here.

def adminlogin(request):
    return render(request,'admin/adminlogin.html')
 

def adminhome(request):
    return render(request,'admin/admin_home.html')
    
def viewconnection(request):
    form=NewconnectionModel.objects.all()
    return render(request,'admin/admin_connection_request.html',{'form':form})

def newconnection_update(request,id):
    number = random.randint(1000,10000)
    form = get_object_or_404(NewconnectionModel,nid=id)
    form.status = 'accept'
    form.uscno=number
    form.save(update_fields=["status"])
    form.save()
    
    #email code
    html_content = "<br/><p>Connection Request Status :<strong> Accepted </strong> your USC No is<strong>" + str(form.uscno) + "</strong></p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [form.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Connection Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent")
    return redirect("viewconnection")

def newconnection_update_reject(request,id):
    number = random.randint(1000,10000)
    form = get_object_or_404(NewconnectionModel,nid=id)
    form.status = 'reject'
    form.uscno=number
    form.save(update_fields=["status"])
    form.save()
    
    html_content = "<br/><p>Connection Request Status :<strong> Rejected </strong> </p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [form.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Connection Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent")
    else:
        print("not valid email")    
    return redirect("viewconnection")

def deletenewconnection(request,id):
    w = NewconnectionModel.objects.filter(nid=id)
    w.delete()
    return redirect('viewconnection')


def viewusercomplaint(request):
    form=RaisecomplaintsModel.objects.all()
    return render(request,'admin/admin_complaints.html',{'form':form})

def deletecomplaint(request,id):
    w = RaisecomplaintsModel.objects.filter(cid=id)
    w.delete()
    return redirect('viewusercomplaint')

def viewfeedback(request):
    form=ServicefeedbackModel.objects.all()
    return render(request,'admin/admin_feedback.html',{'form':form})

def deleteuserfeedback(request,id):
    w = ServicefeedbackModel.objects.filter(sid=id)
    w.delete()
    return redirect('viewfeedback')

def add_biller(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        postalcode=request.POST["postalcode"]
        AddBillerModel.objects.create(name=name,password=password,email=email,mobile=mobile,postalcode=postalcode)
    return render(request,'admin/admin_add_biller.html')

def view_biller(request):
    form=AddBillerModel.objects.all()
    return render(request,'admin/admin_view_biller.html',{'reg':form} )

def removebiller(request,id):
    w = ServicefeedbackModel.objects.filter(sid=id)
    w.delete()
    return redirect('view-biller')

def view_billing(request):
    return render(request,'admin/admin_view_billing.html' )
