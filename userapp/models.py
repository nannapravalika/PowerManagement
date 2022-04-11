from audioop import add
from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from pkg_resources import to_filename

# Create your models here.
class RegistrationModel(models.Model):
    rid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField( )

    def __str__(self):
       return self.name  

    class Meta:
        db_table="Registration-Model"

class NewconnectionModel(models.Model):
    nid = models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50,null=True)
    lastname=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,null=True)
    mobile=models.BigIntegerField( null=True)
    address=models.CharField(max_length=50,null=True)
    category=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    postalcode=models.CharField(max_length=50,null=True)
    apic=models.ImageField( upload_to='images/',null=True)
    ipic=models.ImageField( upload_to='images/',null=True)
    uscno=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=50,default="pending")

    def __str__(self):
       return self.usc 

    class Meta:
        db_table="Newconnection-Model"

class RaisecomplaintsModel(models.Model):
    cid = models.AutoField(primary_key=True)
    usc=models.CharField(max_length=50,null=True)
    fullname=models.CharField(max_length=50,null=True)
    mobile=models.BigIntegerField (null=True)
    email=models.EmailField(max_length=50,null=True)
    complaint=models.TextField(max_length=50,null=True)
    select=models.CharField(max_length=50,null=True)

    def __str__(self):
       return self.fullname 

    class Meta:
        db_table="raisecomplaints-Model"

class ServicefeedbackModel(models.Model):
    sid = models.AutoField(primary_key=True)
    usc=models.CharField(max_length=50,null=True)
    fullname=models.CharField(max_length=50,null=True)
    textarea=models.TextField(max_length=50,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True )
    


    def __str__(self):
       return self.fullname 

    class Meta:
        db_table="Servicefeedback-Model"