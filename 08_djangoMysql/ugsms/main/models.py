from django.db import models
from django.db import connections

# Create your models here.

class aboutDetail(models.Model):
    pageTitle1 = models.CharField(max_length=20)
    pageDescription = models.CharField(max_length=400)
    class Meta:
        db_table = "tblabout"

    def __str__(self):
        return self.pageTitle1

class contactDetail(models.Model):
    pageTitle2 = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    timing = models.CharField(max_length=20)
    class Meta:
        db_table = "tblcontactdetails"
    
    def __str__(self):
        return self.pageTitle2
