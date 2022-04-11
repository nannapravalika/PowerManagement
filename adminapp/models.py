from django.db import models

# Create your models here.
class AddBillerModel(models.Model):
    rid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField( )
    postalcode=models.IntegerField()
    def __str__(self):
       return self.name  

    class Meta:
        db_table="AddBiller-Model"