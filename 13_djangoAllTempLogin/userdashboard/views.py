from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def displayservices(request):
    return render(request, 'dashboard/displayservices.html')

def bookappointment(request):
    return render(request, 'dashboard/bookappointment.html')

def appointmenthistory(request):
    return render(request, 'dashboard/appointmenthistory.html')

def moreappointmenthistory(request):
    return render(request, 'dashboard/moreappointmenthistory.html')

def invoicehistory(request):
    return render(request, 'dashboard/invoicehistory.html')

def moreinvoicehistory(request):
    return render(request, 'dashboard/moreinvoicehistory.html')

def changepassword(request):
    return render(request, 'dashboard/changepassword.html')

def customerprofile(request):
    return render(request, 'dashboard/customerprofile.html')

