from django.shortcuts import render
from django.http import HttpResponse
from main.models import aboutDetail, contactDetail

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')

def about(request):
    aboutdisplay = aboutDetail.objects.all()
    return render(request, 'about.html',{'aboutDetail': aboutdisplay})

def services(request):
    return render(request, 'services.html')

def contact(request):
    contactdisplay = contactDetail.objects.all()
    return render(request, 'contact.html', {'contactDetail': contactdisplay})

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
