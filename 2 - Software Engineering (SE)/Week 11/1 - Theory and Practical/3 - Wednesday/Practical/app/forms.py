# app - forms.py file new

from django import forms
from .models import User

class DateInput(forms.DateInput):
    input_type = 'date'
    
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields =('name','photo','email','password','mobile_number','date_of_birth',)
        widgets = {
        'password': forms.PasswordInput(),
        'date_of_birth': DateInput(),
    }
