from django.shortcuts import render,redirect

from userapp.forms import NewconnectionForm, RegistrationForm
from userapp.models import RaisecomplaintsModel, RegistrationModel,NewconnectionModel, ServicefeedbackModel

# Create your views here.
# def user(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         password = request.POST.get('password')
#         if name =='user' and password =='user':
            
#             return redirect('userhome')
#     return render(request,'user.html  ')

def userlogin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            enter =RegistrationModel.objects.get(name=name,password=password)
            request.session["name"]=enter.rid
            return redirect('userhome')
        except:
            pass
    return render(request,'user/userlogin.html')

def userhome(request):
    return render(request,"user/user_home.html")

def userregister(request):
    form = RegistrationForm()
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        
        RegistrationModel.objects.create(name=name,password=password,email=email,mobile=mobile)
    return render(request,"user/user_register.html")

def newconnection(request):
    form =NewconnectionForm
    if request.method == "POST" and request.FILES['apic']:
         
        firstname = request.POST["fname"]
        lastname = request.POST["lname"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        address=request.POST["address"]
        category=request.POST["category"]
        state=request.POST["state"]
        postalcode=request.POST["postalcode"]
        apic=request.FILES["apic"]
        ipic=request.FILES["ipic"]



        form=NewconnectionForm(request.POST)
         
        form.firstname = firstname
        form.lastname = lastname
        form.email = email
        form.mobile = mobile
        form.address = address
        form.category = category
        form.state = state
        form.postalcode = postalcode
        form.apic = apic
        form.ipic = ipic

        NewconnectionModel.objects.create(firstname=firstname,lastname=lastname,email=email,mobile=mobile,address=address,category=category,state=state,postalcode=postalcode,apic=apic,ipic=ipic)
        return redirect('newconnection')
    else:
        form=NewconnectionModel()
    return render(request,'user/user_new_connection.html',{'form' : form})


def raisecomplaint(request):
    form = RaisecomplaintsModel()
    if request.method == "POST":
        fullname = request.POST["fullname"]
        mobile = request.POST["mobile"]
        email = request.POST["email"]
        complaint = request.POST["remarks"]
        select=request.POST["select"]
        
        RaisecomplaintsModel.objects.create(fullname=fullname,mobile=mobile,email=email,complaint=complaint,select=select)
        return redirect(' raisecomplaint')
    else:
        form=RaisecomplaintsModel()
    return render(request,'user/user_raise_complaint.html')

def servicefeedback(request):
    form = ServicefeedbackModel()
    if request.method == "POST":
        fullname = request.POST["fullname"]
        textarea = request.POST["textarea"]
      
        
        
        ServicefeedbackModel.objects.create(fullname=fullname,textarea=textarea)
        return redirect('servicefeedback')
    else:
        form=ServicefeedbackModel()

    return render(request,'user/user_service_feedback.html')

    
def user_view_bill(request):
    return render(request,"user/user_view_bill.html")

def user_debit(request):
    return render(request,"user/user_debit.html")

def user_credit(request):
    return render(request,"user/user_credit.html")

def user_upi(request):
    return render(request,"user/user_upi.html")
