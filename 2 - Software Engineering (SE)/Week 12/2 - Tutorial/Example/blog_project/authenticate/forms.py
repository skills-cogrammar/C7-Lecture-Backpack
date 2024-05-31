from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    password_conf = forms.CharField(label='Password Confirm', widget=forms.PasswordInput())