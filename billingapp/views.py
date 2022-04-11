from unicodedata import name
from django.shortcuts import render,redirect

from adminapp.models import AddBillerModel
from billingapp.models import GenerateBillModel 
from userapp.models import NewconnectionModel

# Create your views here.

def billerlogin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            enter =AddBillerModel.objects.get(name=name,password=password)
            request.session["rid"]=enter.rid
            return redirect('billinghome')
        except:
            pass
    return render(request,'billing/billinglogin.html')

def billinghome(request):
    return render(request,"billing/billing_home.html")

def billgeneration(request):
    if request.method == "POST":
        x = request.POST.get("uscno")
        obj = NewconnectionModel.objects.filter(uscno=x)
        return render(request,"billing/billing_generate_bill.html", {'obj': obj})
    return render(request,"billing/billing_generate_bill.html" )

# def view_bill_details(request):
#     if request.method == "POST":
#         x = request.POST["uscno"]                   
#         obj = NewconnectionModel.objects.filter(uscno=x)

#     return render(request,"billing/billing_generate_bill.html",{'obj':obj} )


def billingunit(request,id):
    obj = NewconnectionModel.objects.filter(uscno=id)
    # rid=request.session["rid"]
    if request.method=="POST":
        uscno=request.POST.get("uscno")
        units=request.POST.get("units")
        bill=request.POST.get("bill")
        
        GenerateBillModel.objects.create( uscno=uscno,units=units,bill=bill)
        # data = NewconnectionModel.objects.filter(uscno=id)
    return render(request,"billing/billing_units.html", {'obj': obj})