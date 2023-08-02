from django.urls import path
from . import views

#URL Conf
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('displayservices/', views.displayservices, name='displayservices'),
    path('bookappointment/', views.bookappointment, name='bookappointment'),
    path('appointmenthistory/', views.appointmenthistory, name='appointmenthistory'),
    path('appointmenthistory/moreappointmenthistory/', views.moreappointmenthistory, name='moreappointmenthistory'),
    path('invoicehistory/', views.invoicehistory, name='invoicehistory'),
    path('invoicehistory/moreinvoicehistory', views.moreinvoicehistory, name='moreinvoicehistory'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('customerprofile/', views.customerprofile, name='customerprofile'),
    path('customerprofile/customerprofileupdate/', views.customerprofileupdate, name='customerprofileupdate'),
]