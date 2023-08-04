from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import service_Detail

# DISPLAY FROM DATABASE
servicedisplay = service_Detail.objects.all()

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def displayservices(request):
    context = {
        'servicedisplay' : servicedisplay
    }
    return render(request, 'dashboard/displayservices.html', context)

def bookappointment(request):
    # if request.method == "POST":
    #     formApt = appointmentForm(request.POST, request.FILES, instance=request.user.appointmentBooking)
    #     if formApt.is_valid():
    #         formApt.save()
    #         return redirect('appointmenthistory')
    # else:
    #     formApt = appointmentForm(instance=request.user.appointmentBooking)
    # context = {
    #     'formApt': formApt
    # }
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

def customerprofileupdate(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.customerprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('customerprofile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.customerprofile)
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, 'dashboard/customerprofileupdate.html', context)

