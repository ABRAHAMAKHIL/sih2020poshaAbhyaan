from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


class beneficiary_register(models.Model):
    u_user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    u_fname = models.CharField(max_length=30,default=None)
    u_sname = models.CharField(max_length=30,default=None)
    u_father = models.CharField(max_length=30,default=None)
    u_mother = models.CharField(max_length=30,default=None)
    u_adhar = models.CharField(max_length=12,default=None)
    u_pincode = models.CharField(max_length=6,default=None)
    u_addr = models.CharField(max_length=200,default=None)
    u_district = models.CharField(max_length=20,default=None)
    u_phone = models.CharField(max_length=13,default=None)
    u_phno = models.CharField(max_length=13,default=None,null=True,blank=True,unique=True)
    u_type= models.BooleanField(null=True,blank=True,default=False)
    u_DOB = models.DateField(null=True)
    u_status = models.BooleanField(null=True,blank=True,default=False)
    u_verified = models.CharField(max_length=13,null=True,blank=True)
   
    def __str__(self):
        return str(self.u_phno)


class userbmi(models.Model):
    u_user_id= models.CharField(null=True,max_length=14,default=None)
    bmdate=models.DateField(default=date.today())
    currentbmi=models.FloatField(null=True)
    bmweight= models.FloatField(null=True)
    bmheight=models.FloatField(null=True)
    bmblood=models.FloatField(null=True)
    bmworker = models.CharField(max_length=13,null=True,blank=True)

class userappointments(models.Model):
   
    u_user_id= models.CharField(null=True,max_length=14,default=None)
    apdate=models.DateField(null=True)
    apassign = models.CharField(null=True,max_length=10)
    apreceived = models.CharField(null=True,max_length=10)
    apno=models.IntegerField(null=True)
    apPincode= models.CharField(null=True,max_length=10)
    apstatus = models.BooleanField(blank=True,default=False)
    apref = models.CharField(max_length=50,null=True)
    aptype = models.BooleanField(blank=True,default=False)
    apPhone = models.CharField(null=True,max_length=10)





    