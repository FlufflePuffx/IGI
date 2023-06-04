from django import forms
from .models import *


class SignInForm(forms.Form):
    login = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150)
