from django import forms
from django.contrib.auth.models import User
from .models import customerprofile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = customerprofile
        fields = ['address', 'phone', 'image']