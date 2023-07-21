from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def services(request):
    return render(request, 'services.html')

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
    return render(request, 'signup.html', context)

def login(request):
    return render(request, 'login.html')
