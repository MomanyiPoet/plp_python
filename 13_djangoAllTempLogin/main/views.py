from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm

# Create your views here.

def landing_page(request):
    return render(request, 'user/index.html')

def about(request):
    return render(request, 'user/about.html')

def services(request):
    return render(request, 'user/services.html')

def contact(request):
    return render(request, 'user/contact.html')
    
# REGISTRATION OF CLIENTS/USERS
def signup(request):
    # if request.method == "POST":
    #     form = CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('login')
    # else:
    #     form = CreateUserForm()
    # context = {
    #     'form' : form,
    # }
    return render(request, 'user/signup.html',)

def login(request):
    return render(request, 'user/login.html')

def logout(request):
    return render(request, 'user/logout.html')
