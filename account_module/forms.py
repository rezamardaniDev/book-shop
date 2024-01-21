from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'date_of_birth','phone_number', 'password', 'state', 'city', 'city_address']



class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']