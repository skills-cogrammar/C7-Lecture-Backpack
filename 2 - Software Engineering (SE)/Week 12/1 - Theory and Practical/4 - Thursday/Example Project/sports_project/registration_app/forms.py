from django import forms
from django.contrib.auth.models import User
from .models import Registration

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    password_conf = forms.CharField(label='Password Confirm', widget=forms.PasswordInput())


class SportRegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['sport', 'team_name']
