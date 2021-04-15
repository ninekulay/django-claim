from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ClaimPage(models.Model):
	User = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
	Claimid = models.CharField(max_length=100,null=True, blank=True)
	BrandType = models.CharField(max_length=100,null=True, blank=True)
	ModelType = models.CharField(max_length=100,null=True, blank=True)
	SlType  = models.CharField(max_length=100,null=True, blank=True)
	Deliverydate = models.DateTimeField(blank=True,null=True)
	MdSerial  = models.CharField(max_length=20,null=True, blank=True)
	DetailDamage = models.CharField(max_length=800,null=True, blank=True)
	Stamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	Photouser1 = models.FileField(upload_to="photouser1",blank=True,null=True)
	
