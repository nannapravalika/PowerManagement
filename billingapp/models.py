from datetime import datetime
from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class GenerateBillModel(models.Model):
    gid = models.AutoField(primary_key=True)
    bid=models.CharField(max_length=50,null=True)
    uscno=models.IntegerField(max_length=50,null=True)
    units=models.CharField(max_length=50,null=True)
    bill=models.CharField(max_length=50,null=True)
    date_of_bill = models.DateField(auto_now_add=True,null=True)
    # due_date = date_of_bill + timedelta(35)
    bill_status = models.CharField(max_length=100,default='pending')

    
    def __str__(self):
       return self.uscno  

    class Meta:
        db_table="Bill_details"