from django.db import models
# from datetime import datetime
from django.contrib.auth.models import User
# import random, string

# CHOICES
SERVICE_CHOICES = (
    ("Maintenance and Tune-ups", "Maintenance and Tune-ups"),
    ("Brake and Suspension", "Brake and Suspension"),
    ("Diagnostic Services", "Diagnostic Services"),
    ("Not Sure, Select Other", "Not Sure, Select Other"),
)

TIME_CHOICES = (
    ("8 AM", "8 AM"),
    ("10 AM", "10 AM"),
    ("12 AM", "12 AM"),
    ("2 PM", "2 PM"),
    ("4 PM", "4 PM"),
)

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
    
# class appointmentBooking(models.Model):
#     staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     aptNumber = models.CharField(max_length=6, null=True, blank=True)
#     serviceDescription = models.CharField(max_length=100, choices=SERVICE_CHOICES, default="Not Sure, Select Other")
#     aptDate = models.DateField(default=datetime.now)
#     aptTime = models.CharField(max_length=10, choices=TIME_CHOICES, default="2 PM")
#     time_ordered = models.DateTimeField(default=datetime.now, blank=True)
#     class Meta:
#         db_table = "tblappointment"
    
#     def save(self, *args, **kwargs):
#         if not self.aptNumber:
#             self.aptNumber = ''.join(random.choice(string.digits) for _ in range(6))
#         super().save(*args, **kwargs)
    
#     def __str__(self):
#         return self.aptDate
