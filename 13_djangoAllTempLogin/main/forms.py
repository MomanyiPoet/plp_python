from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import contactUs

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class contactUsForm(forms.ModelForm):
    class Meta:
        model = contactUs
        fields = ['firstname', 'lastname', 'mobile', 'message']