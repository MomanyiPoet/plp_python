from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from main.models import aboutDetail, contactDetail
from userdashboard.models import service_Detail
from .forms import CreateUserForm, contactUsForm

# DISPLAY FROM DATABASE
contactdisplay = contactDetail.objects.all()
servicedisplay = service_Detail.objects.all()

# Create your views here.

def landing_page(request):
    return render(request, 'user/index.html')

def about(request):
    aboutdisplay = aboutDetail.objects.all()
    return render(request, 'user/about.html',{'aboutDetail': aboutdisplay})

def services(request):
    context = {
        'servicedisplay' : servicedisplay
    }
    return render(request, 'user/services.html', context)

def contact(request):
    if request.method == "POST":
        formContact = contactUsForm(request.POST)
        if formContact.is_valid():
            formContact.save()
            return redirect('contact')
    else:
        formContact = contactUsForm()
    context = {
        'contactDetail': contactdisplay,
        'formContact': formContact
    }
    return render(request, 'user/contact.html', context)
    
# REGISTRATION OF CLIENTS/USERS
def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {
        'form' : form,
    }
    return render(request, 'user/signup.html', context)

def login(request):
    return render(request, 'user/login.html', {'contactDetail': contactdisplay})

def logout(request):
    return render(request, 'user/logout.html')
