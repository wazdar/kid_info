from django import forms
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterNewInstitutionAndUser(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=256)

    #TODO dokończyć formularz