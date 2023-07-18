from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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

# Login Authentication
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user using Django's authentication system
        user = authenticate(username=username, password=password)

        if user is not None:
            # Successful login, log the user in and store the user in the session
            login(request, user)
            return redirect('services')  # Redirect to the user's home page
        else:
            # Failed login, show an error message
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

# SignUp Authentication
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Create a new user using Django's User model and save it to the database
        user = User.objects.create_user(username=username, password=password)

        return redirect('login')  # Redirect to the user's home page after successful signup
    else:
        return render(request, 'signup.html')
