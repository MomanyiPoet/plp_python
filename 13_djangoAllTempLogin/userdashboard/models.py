from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customerprofile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_images')

    def __str__(self):
        return self.staff.username
    
class service_Detail(models.Model):
    servicename = models.CharField(max_length=50)
    servicedescription = models.CharField(max_length=200)
    cost = models.CharField(max_length=20)
    image = models.ImageField(default='bg23.jpg', upload_to='service_images')
    creationdate = models.DateTimeField()
    class Meta:
        db_table = "tblservices"
    
    def __str__(self):
        return self.servicename
    
# class appointmentBook(models.Model):
#     userID = models.CharField(max_length=50)
#     aptNumber = models.CharField(max_length=200)
#     aptDate = models.CharField(max_length=20)
#     aptTime = models.ImageField(default='bg23.jpg', upload_to='service_images')
#     creationdate = models.DateTimeField()
#     class Meta:
#         db_table = "tblservices"
    
#     def __str__(self):
#         return self.servicename
