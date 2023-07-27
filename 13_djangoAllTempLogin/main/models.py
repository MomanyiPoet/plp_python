from django.db import models

# Create your models here.
class aboutDetail(models.Model):
    pageName = models.CharField(max_length=20)
    pageDescription = models.CharField(max_length=500)
    class Meta:
        db_table = "tblabout"

    def __str__(self):
        return f'{self.pageName} - {self.pageDescription}'

class contactDetail(models.Model):
    pagename = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    timing = models.CharField(max_length=20)
    class Meta:
        db_table = "tblcontactdetails"
    
    def __str__(self):
        return f'{self.pagename} - {self.email} - {self.mobile} - {self.address} - {self.timing}'
